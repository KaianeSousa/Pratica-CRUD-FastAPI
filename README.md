# 🩸 Sistema de Cadastro de Doadores

Este projeto simula um sistema para gerenciamento de doadores e receptores de sangue, desenvolvido com o framework FastAPI, permitindo a criação e gestão de informações de maneira eficiente e organizada. Ele utiliza as operações CRUD (Create, Read, Update e Delete) para manipular dados de doadores e receptores.

Além de gerenciar informações básicas como nome, idade e tipo sanguíneo, o sistema conta com uma lógica para validação de compatibilidade sanguínea. Essa funcionalidade assegura que as doações sejam realizadas para os tipos sanguíneos correspondentes, respeitando as regras biológicas entre os diferentes tipos sanguíneos, incluindo situações especiais, como indivíduos com o raro "sangue dourado" (Rh nulo). Este tipo sanguíneo, devido à sua extrema raridade, pode doar para praticamente qualquer pessoa, mas só pode receber sangue do mesmo grupo.

---

## 📋 Funcionalidades

### **Gerenciamento de Doadores**
- **Cadastrar doador:** Adicione informações como nome, idade e tipo sanguíneo de um novo doador.
- **Consultar doadores:** Liste todos os doadores cadastrados ou realize consultas por ID.
- **Atualizar doador:** Atualize os dados de um doador já existente.
- **Excluir doador:** Remova um doador cadastrado do sistema.

### **Gerenciamento de Receptores**
- **Cadastrar receptor:** Insira informações sobre receptores, como nome, idade e tipo sanguíneo.
- **Consultar receptores:** Liste todos os receptores cadastrados ou realize consultas por ID.
- **Atualizar receptor:** Atualize os dados de um receptor já existente.
- **Excluir receptor:** Remova um receptor cadastrado do sistema.

### **Gerenciamento de Doações**
- **Verificar compatibilidade sanguínea:**  
  - O sistema valida automaticamente a compatibilidade entre doador e receptor com base na **tabela de compatibilidade sanguínea**.
  - Tipos sanguíneos suportados:  
    - A+, A-, B+, B-, AB+, AB-, O+, O- e Rh nulo (sangue dourado).

- **Casos especiais:**
  - **Rh nulo (sangue dourado):**  
    - Pode doar para qualquer um.
    - Pode receber apenas Rh nulo.  

---

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3.12.5
- **Framework Web:** FastAPI
- **Template:** Jinja2
- **Container:** Docker
- **Servidor:** Uvicorn
- **IDE:** PyCharm  

---

## 🚀 Como o Sistema Funciona

### 1. **Cadastro de Doadores e Receptores**
Insira informações básicas do doador/receptor, como:
  - Nome
  - Idade
  - Tipo sanguíneo  
O sistema valida automaticamente:
  - Idade dos doadores (16 a 69 anos).
  - Tipos sanguíneos inseridos.

### 2. **Consulta de Doadores e Receptores**
- Liste todos os doadores ou receptores cadastrados.
- Consulte informações específicas usando o **ID**.

### 3. **Atualização e Exclusão**
- **Atualize:** Modifique dados de um doador ou receptor já cadastrado.
- **Exclua:** Remova qualquer registro de doador ou receptor.

### 4. **Validação de Doações**
- Insira o **ID do doador** e o **ID do receptor**.
- O sistema verificará se a doação é compatível, seguindo as regras de compatibilidade:
  - A tabela de compatibilidade sanguínea é utilizada.
  - Tipos especiais como Rh nulo recebem validações específicas.

### 5. **Compatibilidade com Rh Nulo**
- **Doadores com Rh nulo:**
  - Podem doar apenas para outros Rh nulos.
- **Receptores com Rh nulo:**
  - Podem receber de qualquer Rh nulo ou do tipo O-.

---

## 🩺 Tabela de Compatibilidade Sanguínea

| Tipo Sanguíneo | Pode doar para           | Pode receber de         |
|----------------|--------------------------|--------------------------|
| **A+**         | AB+, A+                  | A+, A-, O+, O-           |
| **A-**         | A+, A-, AB+, AB-         | A-, O-                   |
| **B+**         | B+, AB+                  | B+, B-, O+, O-           |
| **B-**         | B+, B-, AB+, AB-         | B-, O-                   |
| **AB+**        | AB+                      | Todos os tipos           |
| **AB-**        | AB+, AB-                 | A-, B-, AB-, O-          |
| **O+**         | A+, B+, AB+, O+          | O+, O-                   |
| **O-**         | Todos os tipos           | O-                       |
| **Rh nulo**    | Apenas Rh nulo           | Rh nulo                  |

---

## 💻 Criando o ambiente virtual
- Recomendado: Crie um diretório para executar o servidor
```bash
  mkdir servidor_fastapi
 ```

- Entre no diretório criado
```bash
  cd servidor_fastapi
```

- Criando ambiente
```bash
  python -m venv venv
```

- __*Ativando ambiente*__

**Windows**
```bash
  venv\Scripts\activate
```

**Linux/macOS:**
```bash
  source venv/bin/activate
```

#### Caso não queria configurar um ambiente, basta baixar o Pycharm: https://www.jetbrains.com/pycharm/ e executar
```bash
  charm .
```

- #### Instale as dependências: FastAPI e servidor Unicorn
```bash
  pip install fastapi uvicorn
```

**Abra algum editor de código com terminal, como:**

Visual Studio Code
```bash
  code .
```
Intellij
```bash
  idea .
```
- Subir no Docker
```bash
docker-compose up -d --build doacoes
```

- Crie um arquivo main.py, cole o código do arquivo com o mesmo nome neste repositório e o execute com
```bash
  uvicorn main:app --reload
```

**Ou, se preferir, basta fazer o git clone deste projeto**
```bash
  git@github.com:KaianeSousa/Pratica-CRUD-FastAPI.git
```
---
## 🛣️ Rotas no Postman

Link da coleção: https://www.postman.com/kay-yak/workspace/fastapi/collection/40103969-ecd0c70d-6fd5-4275-965f-b44ad1bf2872?action=share&creator=40103969

## 🚀 Rodando o projeto

- ### Doadores 👥

  ### Código JSON de entrada:
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

### 1. **Cadastrar doador** 📋
**POST** `/doadores/adicionar`

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
```

- **Resposta caso não exista doador cadastrado:**
```json
{
    "detail": "Doador não encontrado"
}
```

### 4. **Atualizar informações do doador** 📋

**PUT** `/doadores/atualizar/{doador_id}`

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

### 5. **Deletar doador** 📋

**DELETE** `/doadores/{doador_id}`

Deleta o doador e seus dados.

- **Resposta:**
```json
{
    "detail": "Doador removido com sucesso"
}
```
---
- ### Recebedores  👩‍🦳👨👧

    ### Código JSON de entrada:
```json
{
    "mensagem": "Recebedor cadastrado com sucesso:",
    "recebedor": {
        "id": 1,
        "nome": "Joana",
        "idade": 26,
        "tipo_sanguineo": "O+",
        "necessidades_de_sangue": "Cirurgia"
    }
}
```

### 1. **Cadastrar recebedor** 📋
**POST** `/recebedores/adicionar`

Cadastra um novo recebedor.

- **Resposta**
```json
{
    "mensagem": "Recebedor cadastrado com sucesso:",
    "recebedor": {
        "id": 1,
        "nome": "Joana",
        "idade": 26,
        "tipo_sanguineo": "O+",
        "necessidades_de_sangue": "Cirurgia"
    }
}
```

- **Resposta, caso já exista um recebedor com o ID:**
```json
{
    "detail": "Já existe um recebedor com este ID: 1"
}
```
  
### 2. **Listar todos os recebedores** 📋

**GET** `/recebedores`

Retorna uma lista com todos os recebedores cadastrados.

- **Resposta:**
```json
{
 "mensagem": "Lista de todos os recebedores disponíveis:",
    "recebedores": [
        {
            "id": 1,
            "nome": "Joana",
            "idade": 26,
            "tipo_sanguineo": "O+",
            "necessidades_de_sangue": "Cirurgia"
        }
    ]
}
```

- **Resposta caso não exista recebedor cadastrado:**
```json
{
    "detail": "Nenhum recebedor encontrado."
}
```
      
### 3. **Listar recebedor pelo ID** 📋

**GET** `/recebedores/{recebedor_id}`

Retorna o doador cadastrado referente ao seu ID.

**Resposta:**
```json
{
    "mensagem": "Recebedor encontrado com sucesso:",
    "recebedor": {
        "id": 1,
        "nome": "Joana",
        "idade": 26,
        "tipo_sanguineo": "O+",
        "necessidades_de_sangue": "Cirurgia"
    }
}
```

- **Resposta caso não exista doador cadastrado:**
```json
{
    "detail": "Recebedor não encontrado"
}
```

### 4. **Atualizar informações do recebedor** 📋

**PUT** `/recebedores/atualizar/{recebedor_id}`

Permite modificar os dados do recebedor.

- **Resposta:**
```json
{
    "mensagem": "Dados do recebedor atualizados com sucesso:",
    "recebedor": {
        "id": 1,
        "nome": "Joana",
        "idade": 27,
        "tipo_sanguineo": "O-",
        "necessidades_de_sangue": "Cirurgia"
    }
}
```

### 5. **Deletar doador** 📋

**DELETE** `/recebedores/{recebedor_id}`

Deleta o recebedor e seus dados.

- **Resposta:**
```json
{
    "detail": "Recebedor removido com sucesso"
}
```
---
- ### Doação 💉

**POST** `/doacao/`

Encontra o doador com o sangue compatível ao do recebedor.

**Entrada**
```json
{
  "doador_id": 1,
  "recebedor_id": 1
}
```

**Resposta**
```json
{
    "mensagem": "Doação compatível de Beatriz para Joana"
}
```

- **Resposta, caso os sangues sejam incompatíveis:**
```json
{
    "detail": "Incompatibilidade: O+ não pode doar para Rh-nulo"
}
```
  




