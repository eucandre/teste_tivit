Aqui está um exemplo de `README.md` para o seu projeto FastAPI com SQLAlchemy, autenticação JWT e integração com o pytest para testes. O guia inclui instruções de instalação, configuração e como rodar os testes.

---

# Projeto FastAPI com Autenticação e Testes

Este é um projeto FastAPI que implementa autenticação básica com JWT, banco de dados SQLAlchemy e inclui testes de unidade para validação de funcionalidades.

## Sumário

- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração do Banco de Dados](#configuração-do-banco-de-dados)
- [Execução do Projeto](#execução-do-projeto)
- [Testes e Cobertura de Código](#testes-e-cobertura-de-código)
- [Estilo de Código](#estilo-de-código)
- [Utilização da API](#utilizacao-da-api)

## Pré-requisitos

- Python 3.10 ou superior
- [Poetry](https://python-poetry.org/docs/#installation) (opcional, mas recomendado para gerenciar dependências)
- Banco de Dados (sqlite)


## Instalação

1. Clone o repositório para sua máquina local:

    ```
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Crie e ative um ambiente virtual:

    ```
    python3 -m venv venv ou virtualenv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. Instale as dependências:

    Se estiver usando o `poetry`:

    ```
    poetry install
    ```

    Ou com `pip`:

    ```
    pip install -r requirements.txt
    ```

## Configuração do Banco de Dados

1. Configure o banco de dados (use `.env.example` como referência para criar um arquivo `.env`):

    ```
    cp .env.example .env
    ```

2. Edite o arquivo `.env` com suas credenciais e informações do banco de dados.


## Execução do Projeto

Execute ppython create_users.py na raiz do projeto

Para iniciar o servidor FastAPI, use o comando:

```
uvicorn app.main:app --reload
```

O projeto estará disponível em `http://127.0.0.1:8000`.

## Testes e Cobertura de Código

1. Instale o pacote `pytest` e `pytest-cov` para execução dos testes e cobertura de código:

    ```
    pip install pytest pytest-cov
    ```

2. Para rodar os testes, utilize:

    ```
    pytest
    ```

3. Para gerar um relatório de cobertura de código em HTML:

    ```
    pytest --cov=app --cov-report=html
    ```

    Após a execução, você pode abrir o relatório gerado em `htmlcov/index.html`.

## Estilo de Código

Para garantir que o código está em conformidade com o PEP 8, instale e utilize o `flake8`:

```
pip install flake8
```

Para executar o `flake8` em seu código, utilize:

```
flake8 app/
```

---

## Utilização da API
1. curl -X POST "http://127.0.0.1:8000/token" -H "Content-Type: application/json" -d '{"username": "user", "password": "L0XuwPOdS5U"}'
2. curl -X GET "http://127.0.0.1:8000/user" -H "Authorization: Bearer <seu_token_aqui>"
3. curl -X GET "http://127.0.0.1:8000/admin" -H "Authorization: Bearer <seu_token_aqui>"

---

## Estrutura do Projeto

Aqui está uma visão geral da estrutura de diretórios e arquivos do projeto:


├── app
│   ├── main.py                # Arquivo principal do FastAPI
│   ├── models.py              # Modelos do SQLAlchemy
│   ├── database.py            # Configuração do banco de dados
│   ├── auth.py                # Funções de autenticação e rotas de login
│   ├── config.py              # Configurações 
|   ├── schema.py              # Esquemas do banco de dados
|   ├── test_main.py           # Testes do app  
├── .env.example               # Exemplo de arquivo de configuração
├── requirements.txt           # Dependências do projeto
├── README.md                  # Documentação do projeto


Siga estes passos para configurar e rodar o projeto com sucesso. Se tiver dúvidas, consulte a [documentação do FastAPI](https://fastapi.tiangolo.com/) para mais informações.