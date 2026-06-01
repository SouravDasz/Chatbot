from fastapi import FastAPI,Request,Form
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
from mechanizm import model

template=Jinja2Templates(directory=r"C:\chatbot\templates")
app=FastAPI()

@app.get("/")
def home(request:Request):
    return template.TemplateResponse(request,name="home.html")

chat_list=[]

@app.get("/chat")
def chat(request:Request):
    return template.TemplateResponse(request,name="chat.html",context={"chat_list":chat_list})

@app.post('/chat')
def caht(request:Request,message:str=Form(...)):
    chat_list.append(message)
    result=model.invoke(message)
    chat_list.append(result.content)
    return RedirectResponse(status_code=303,url="/chat")