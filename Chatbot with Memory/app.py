from fastapi import FastAPI,Request,Form
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.messages import HumanMessage,AIMessage
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from mechanism import model

app=FastAPI()

template=Jinja2Templates(directory=r"C:\chatbot\Chatbot with Memory\templates")

prompt=ChatPromptTemplate.from_messages([
    ("system","you are a help ful AI assistant"),
    MessagesPlaceholder(variable_name="history"),
    ("human","{question}")
])



@app.get("/")
def home(request:Request):
    return template.TemplateResponse(request=request,name="home.html")
history=[]
@app.get("/chat")
def chat(request:Request):
    return template.TemplateResponse(request,name="chat.html",context={"chat_list":history})

@app.post("/chat")
def chat(request:Request,message:str=Form(...)):

    question=message
    prompt_value=prompt.invoke({"question":question,"history":history})
    history.append(
        HumanMessage(content=question)
    )

    response=model.invoke(prompt_value)

    history.append(
        AIMessage(content=response.content)
    )
    return template.TemplateResponse(request,name="chat.html",context={
        "chat_list":history,"prompt_value":prompt_value
    })