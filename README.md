**Sistema de Conciliação Financeira — API + Dashboard**

Este projeto é um sistema completo de **conciliação financeira**, composto por:

Uma **API em FastAPI** para processamento e comparação de planilhas CSV.
Um **dashboard em Streamlit** permitindo upload de arquivos, exibição da tabela conciliada e métricas visuais.

Ideal para estudos, portfolio e demonstração de integração entre backend e frontend utilizando Python.

**🚀 Funcionalidades**

**🔙 Backend (FastAPI)**

• Endpoint para conciliação de dois arquivos CSV
• Regras de comparação:
    •Valores iguais ou com diferença menor que 1
    •Mesma data
    •Classificação automática:
        **• Conciliado**
        **• Divergente**
        **• Não encontrado**
• Retorno em JSON

**🎨 Frontend (Streamlit)**

• Upload de dois arquivos CSV
• Botão para enviar os arquivos para a API
• Tabela estilizada com cores:
    • Verde → Conciliado
    • Vermelho → Divergente
    • Amarelo → Não encontrado
• Resumo com contagem de status
• Tratamento de erro caso a API esteja offline

**📂 Estrutura do Projeto**

📦 sistema-conciliacao
├── backend
│   ├── main.py
│   ├── services
│   │   └── conciliacao.py
│   └── requirements.txt
└── frontend
└── app.py

**🛠️ Tecnologias Utilizadas**

**Backend**
• Python
• FastAPI
• Uvicorn

**Processamento de Dados**
• Pandas

**Frontend**
• Streamlit

**Comunicação**
• Requests

**▶️ Como rodar o projeto**

**1. Clone o repositório**

git clone https://github.com/<seu-usuario>/<seu-repo>.git
cd <seu-repo>

**🖥️ Rodando o Backend (FastAPI)**
1. Acesse a pasta:
cd backend

2. Ative a venv (Windows):
venv\Scripts\activate

3. Instale as dependências:
pip install -r requirements.txt

4. Rode o servidor:
python -m uvicorn main:app --reload

A API estará disponível em:
👉 http://127.0.0.1:8000

Documentação automática (Swagger):
👉 http://127.0.0.1:8000/docs

**🧩 Rodando o Frontend (Streamlit)**

1. Vá para a pasta:
cd frontend

2. Execute:
streamlit run app.py

Interface estará disponível em:
👉 http://localhost:8501

**📊 Exemplo de Resultado da Conciliação**

[
  {
    "data": "2026-03-01",
    "valor": 100,
    "descricao": "mercado",
    "status": "Conciliado"
  },
  {
    "data": "2026-03-02",
    "valor": 200,
    "descricao": "energia",
    "status": "Divergente"
  }
]
