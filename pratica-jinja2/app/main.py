from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.security import OAuth2PasswordBearer
from app.auth import validar_token
from app.routes import auth, doadores, recebedores, doacoes

import uvicorn
from app.database import engine
from app.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

origins = ["http://localhost:8000"]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def verificar_usuario(token: str = Depends(oauth2_scheme)):
    """ Verifica se o usuário está autenticado antes de acessar uma rota protegida. """
    try:
        dados = validar_token(token)
        return dados
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))

app.include_router(auth.router, prefix="/auth")

@app.get("/protegido", dependencies=[Depends(verificar_usuario)])
async def rota_protegida():
    return {"mensagem": "Você acessou uma rota protegida!"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/cadastrar", response_class=HTMLResponse)
async def cadastrar_page(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@app.get("/recuperarSenha", response_class=HTMLResponse)
async def recuperarSenha_page(request: Request):
    return templates.TemplateResponse("recuperarSenha.html", {"request": request})

@app.get("/index", response_class=HTMLResponse)
async def index_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/doadores", response_class=HTMLResponse)
async def doadores_page(request: Request):
    return templates.TemplateResponse("doadores.html", {"request": request})

@app.get("/recebedores", response_class=HTMLResponse)
async def recebedores_page(request: Request):
    return templates.TemplateResponse("recebedores.html", {"request": request})

app.get("/doacoes", response_class=HTMLResponse)
async def doacoes_page(request: Request):
    return templates.TemplateResponse("doacoes.html", {"request": request})

app.include_router(doadores.router, prefix="/doadores")
app.include_router(recebedores.router, prefix="/recebedores")
app.include_router(doacoes.router, prefix="/doacoes")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
