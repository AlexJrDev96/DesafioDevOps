# DesafioDevOps

Repositório do desafio da matéria DevOps --- contém uma aplicação em
Python + Docker + testes, seguindo requisitos do exercício.

## 📁 Estrutura do projeto

    .
    ├── Dockerfile
    ├── docker-compose.yml
    ├── app.py
    ├── requirements.txt
    ├── test_app.py
    ├── static/             # Arquivos estáticos (se houver)
    ├── .github/workflows/  # Configurações de CI/CD (GitHub Actions)
    └── …                   # Outras pastas / arquivos gerados

## 🚀 Como rodar localmente

### Pré-requisitos

-   Docker e docker‑compose instalados\
-   (Opcional) Python 3.8+ + virtualenv, caso queira rodar sem Docker

### Com Docker (recomendado)

``` bash
docker-compose up --build
```

### Sem Docker (modo de desenvolvimento)

``` bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

## ✅ Testes

``` bash
pytest test_app.py
```

## 🧑‍💻 Detalhes do desafio / contexto

Desafio da disciplina de DevOps --- o objetivo é demonstrar habilidades
de containerização, automação, testes e deployment.

## 📬 Contato / Autor

-   Autor: **AlexJrDev96**
-   GitHub: https://github.com/AlexJrDev96/DesafioDevOps
