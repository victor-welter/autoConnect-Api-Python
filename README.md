# API REST AutoConnect

API desenvolvida para a Prática Profissional III do 8° semestre do curso de Engenharia de Computação - SETREM.

## Descrição

Esta API foi desenvolvida para fornecer endpoints para gerenciar dados de automóveis e seus proprietários.

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

## Executando a API

3. **Inicie a API** usando o Uvicorn e o ngrok:
   ```bash
   uvicorn main:app --reload
   ```

   O parâmetro `--reload` permite que o servidor reinicie automaticamente quando você fizer alterações no código.

   ```bash
   ngrok http 8000 
   ```

   O ngrok é um serviço que permite acessar a API localmente de forma segura.

## Documentação Automática

O FastAPI gera automaticamente a documentação da API. Você pode acessá-la em:

- [Swagger UI](http://127.0.0.1:8000/docs)
- [ReDoc](http://127.0.0.1:8000/redoc)

## Detalhes Interessantes

- **FastAPI** é baseado em Python type hints, o que facilita a validação de dados e a documentação automática.
- O **Uvicorn** é um servidor ASGI que permite a execução de aplicações assíncronas.
- O FastAPI suporta WebSockets e muito mais, o que o torna uma excelente escolha para aplicações modernas.
- O Ngrok é uma ferramenta útil para testar aplicações localmente antes de implantar.

## Contribuindo

Se você quiser contribuir para este projeto, sinta-se à vontade para enviar pull requests ou abrir issues para discutir melhorias!

## Licença

Este projeto está sob a [MIT License](LICENSE).
