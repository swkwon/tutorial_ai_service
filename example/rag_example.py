from langserve import RemoteRunnable
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain import hub
from langchain_core.runnables import RunnablePassthrough
import os
os.environ['CURL_CA_BUNDLE'] = ''


loader = PyPDFLoader(r"대한민국헌법(헌법)(제00010호)(19880225).pdf")
pages = loader.load_and_split()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
docs = text_splitter.split_documents(pages)

model_name = "jhgan/ko-sbert-nli"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': True}
# 허깅페이스 관련 SSL 에러
# https://stackoverflow.com/questions/75110981/sslerror-httpsconnectionpoolhost-huggingface-co-port-443-max-retries-exce
embedding = HuggingFaceEmbeddings(
    model_name=model_name, 
    model_kwargs=model_kwargs, 
    encode_kwargs=encode_kwargs
    )

vectorstore = Chroma.from_documents(docs, embedding)
retriever = vectorstore.as_retriever()
prompt = hub.pull("rlm/rag-prompt")

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

llm = RemoteRunnable("http://localhost:8000/llm")

rag_chain = (
    {"context": retriever|format_docs, "question": RunnablePassthrough()}
     | prompt
     | llm
     | StrOutputParser()
)

for chunk in rag_chain.stream("대한민국에는 어떤 행정부가 있지?"):
    print(chunk, end="", flush=True)