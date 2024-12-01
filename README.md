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

- **Resposta, caso a idade esteja entre 16 e 69 anos:**
```json
{
    "mensagem": "Doador cadastrado com sucesso:",
    "doador": {
        "id": 1,
        "nome": "Beatriz",
        "idade": 16,
        "tipo_sanguineo": "O-",
        "data_da_ultima_doacao": "23-06-2021"
    }
}
```

- **Resposta, caso a idade seja menor que 16 ou maior que 69 anos:**
```json
{
    "detail": "Idade inválida! O doador deve ter entre 16 e 69 anos."
}
```

- **Resposta, caso já exista um doador com o ID:**
```json
{
    "detail": "Já existe um doador com este ID: 1"
}
```
  
### 2. **Listar todos os doadores** 📋

**GET** `/doadores`

Retorna uma lista com todos os doadores cadastrados.

- **Resposta:**
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

- **Resposta caso não exista doador cadastrado:**
```json
{
    "detail": "Nenhum doador encontrado."
}
```
      
### 3. **Listar doador pelo ID** 📋

**GET** `/doadores/{doador_id}`

Retorna o doador cadastrado referente ao seu ID.

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

- **Resposta caso não exista doador cadastrado:**
```json
{
    "detail": "Doador não encontrado"
}
```

### 4. **Atualizar informações do doador** 📋

**PUT** `/doadores/{doador_id}`

Permite modificar os dados do doador.

- **Resposta:**
```json
{
    "mensagem": "Dados do doador atualizados com sucesso:",
    "doador": {
        "id": 1,
        "nome": "Beatriz",
        "idade": 17,
        "tipo_sanguineo": "O-",
        "data_da_ultima_doacao": "23-06-2021"
    }
}
```

- **Resposta caso o doador não exista:**
```json
{
    "detail": "Doador não encontrado"
}
```

### 5. **Deletar doador** 📋

**DELETE** `/doadores/{doador_id}`

Deleta os dados do doador.

- **Resposta:**
```json
{
    "detail": "Doador removido com sucesso"
}
```






