
# API com FastAPI

Este projeto é uma API simples construída usando o **FastAPI** e **Uvicorn**. A API responde a solicitações HTTP e pode ser facilmente expandida para atender a requisitos mais complexos.

## Pré-requisitos

Antes de começar, você precisará ter o seguinte instalado:

- Python 3.6 ou superior
- Pipenv (para gerenciar dependências)
- FastAPI
- Uvicorn

## Instalando Dependências

1. **Crie um ambiente virtual** (caso ainda não tenha feito):
   ```bash
   pipenv install
   ```

2. **Instale as dependências**:
   ```bash
   pipenv install fastapi uvicorn
   ```

## Estrutura do Projeto

O projeto deve ter a seguinte estrutura:

```
autoConnect-API/
│
├── env/                  # Ambiente virtual criado pelo Pipenv
│
├── main.py              # Arquivo principal da API
│
└── Pipfile               # Arquivo de gerenciamento de dependências
```

## Criando a API

1. **Crie o arquivo principal da API**:
   ```bash
   touch main.py
   ```

2. **Adicione o seguinte código ao `main.py`**:

   ```python
   from fastapi import FastAPI

   app = FastAPI()

   @app.get("/")
   def read_root():
       return {"message": "Bem-vindo à API com FastAPI!"}

   @app.get("/items/{item_id}")
   def read_item(item_id: int):
       return {"item_id": item_id}
   ```

## Executando a API

3. **Inicie a API** usando o Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

   O parâmetro `--reload` permite que o servidor reinicie automaticamente quando você fizer alterações no código.

## Testando a API

4. **Acesse a API** em seu navegador:
   ```
   http://127.0.0.1:8000/
   ```
   Você verá a resposta:
   ```json
   {"message": "Bem-vindo à API com FastAPI!"}
   ```

5. **Teste um endpoint com parâmetro**:
   Acesse:
   ```
   http://127.0.0.1:8000/items/1
   ```
   A resposta deve ser:
   ```json
   {"item_id": 1}
   ```

## Documentação Automática

O FastAPI gera automaticamente a documentação da API. Você pode acessá-la em:

- [Swagger UI](http://127.0.0.1:8000/docs)
- [ReDoc](http://127.0.0.1:8000/redoc)

## Detalhes Interessantes

- **FastAPI** é baseado em Python type hints, o que facilita a validação de dados e a documentação automática.
- O **Uvicorn** é um servidor ASGI que permite a execução de aplicações assíncronas.
- O FastAPI suporta WebSockets e muito mais, o que o torna uma excelente escolha para aplicações modernas.

## Contribuindo

Se você quiser contribuir para este projeto, sinta-se à vontade para enviar pull requests ou abrir issues para discutir melhorias!

## Licença

Este projeto está sob a [MIT License](LICENSE).
