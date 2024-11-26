from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Union, Any, Dict
from pydantic import BaseModel, Field
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langserve import add_routes
from chain import chain
from chat import chain as chat_chain
from translator import chain as translator_chain
from llm import llm as model

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/chat/playground")

add_routes(app, chain, path="/prompt")

class InputChat(BaseModel):
    """Input for the chat endpoint."""
    
    messages: List[Union[HumanMessage, AIMessage, SystemMessage]] = Field(
        ..., description="Messages to chat with the AI"
    )

add_routes(
    app,
    chat_chain.with_types(input_type=InputChat),
    path="/chat",
    enable_feedback_endpoint=True,
    enable_public_trace_link_endpoint=True,
    playground_type="chat",
)
add_routes(app, translator_chain, path="/translator")
# class InputTranslate(BaseModel):
#     """Input for the translator endpoint."""
#     input: str = Field(..., description="Text to translate")
# add_routes(
#     app,
#     translator_chain.with_types(input_type=InputTranslate),
#     path="/translator",
#     enable_feedback_endpoint=True,
#     enable_public_trace_link_endpoint=True,
#     playground_type="default",
# )
add_routes(app, model, path="/llm")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)