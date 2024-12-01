# Sistema de Cadastro de Doadores
Este projeto é um sistema para gerenciamento de doadores, desenvolvido com FastAPI para criar e gerenciar doadores utilizando as operações CRUD (Create, Read, Update e Delete). 
O sistema valida que os doadores estejam dentro da faixa etária permitida e fornece uma interface interativa para visualização das rotas.

## 📋 Funcionalidades
- Cadastrar doador: Adicione informações sobre um novo doador.
- Consultar doadores: Liste todos os doadores cadastrados ou consulte por ID.
- Atualizar doador: Atualize os dados de um doador existente.
- Excluir doador: Remova um doador cadastrado.
- Validação de idade: Apenas doadores entre 16 e 69 anos podem ser cadastrados.

## 🛠️ Tecnologias Utilizadas
- Linguagem: Python 3.12.5
- Framework Web: FastAPI
- Servidor: Uvicorn

## 💻 Requisitos para Rodar o Projeto
- Python 3.10 ou superior
- Pip (gerenciador de pacotes do Python)
- Um ambiente virtual configurado

## 🚀 Rodando o Projeto

### 1. **Cadastrar doador** 📋
**POST** `/doadores`

Cadastra um novo doador.

- **Resposta (caso a idade esteja entre 16 e 69 anos):**
```json
{
    "mensagem": "Sucesso ao listar doadores:",
    "doadores": [{ "id": 1,
                  "nome": "Lara",
                  "idade": 24,
                  "tipo_sanguineo": "AB",
                  "data_da_ultima_doacao": "16-02-2021"
}]
}
```
- **Resposta (caso a idade seja menor que 16 ou maior que 69 anos):**
```json
{
    "detail": "Idade inválida! O doador deve ter entre 16 e 69 anos."
}
```
  
### 2. **Listar todos os doadores** 📋

**GET** `/doadores`

Retorna uma lista com todos os doadores cadastrados.

**Resposta:**
```json
{
    "mensagem": "Lista de todos os doadores disponíveis:",
    "doadores": [
        {
            "id": 1,
            "nome": "Beatriz",
            "idade": 16,
            "tipo_sanguineo": "O-",
            "data_da_ultima_doacao": "23-06-2021"
        }
    ]
}
```
### 2. **Listar doador pelo ID** 📋

**GET** `/doadores/1`

Retorna o doador cadastro referente ao seu ID.

**Resposta:**
```json
{
    "mensagem": "Doador encontrado com sucesso:",
    "doador": {
        "id": 1,
        "nome": "Beatriz",
        "idade": 16,
        "tipo_sanguineo": "O-",
        "data_da_ultima_doacao": "23-06-2021"
    }
}
}
```
