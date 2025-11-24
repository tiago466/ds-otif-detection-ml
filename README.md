# 🚚 Previsão de Atrasos na Cadeia Logística da Zenatur (Case SOLID)

### Faculdade Impacta — Fundamentos de Machine Learning  
**Professor:** Vinícius Vale  
**Aluno:** *Tiago Pereira Lima* | **RA:** *1020325*  
**Semestre:** 2025/2

---

## 🧠 Visão Geral

Este projeto aplica Machine Learning para prever atrasos de entrega (On Time) dentro do indicador estratégico OTIF (On Time In Full) da empresa Zenatur Logística.
A solução foi construída como entrega oficial do Trabalho de Fundamentos de ML e MVP real corporativo para stakeholders da Zenatur (via SOLID Consultoria)

A solução abrange:

- Pipeline CRISP-DM completo  
- EDA descritiva + inferencial  
- Pré-processamento profissional com sklearn  
- Tratamento de desbalanceamento extremo  
- Treinamento de modelos clássicos e avançados  
- Otimização de threshold por custo de erro  
- Interpretação com SHAP  
- Deploy em **API FastAPI** e **aplicativo Streamlit/Gradio**  
- Estrutura modular e reprodutível para GitHub  

---

## 🎯 Objetivo

Desenvolver um sistema robusto de detecção de fraude baseado em dados, capaz de:

- Prever se um pedido será entregue no prazo ou fora do prazo  
- Estimar o risco de atraso com base nas etapas operacionais  
- Sugerir ações operacionais preventivas  
- Disponibilizar uma interface simples (API + Dashboard)

---

## 📦 Dataset

**Fonte:** Informações de pedidos e acompanhamento operacional banco de dados SQL Server

- **284.807** registros  
- **492** casos fora do prazo  

---

# 🧭 Navegação do Projeto

> Toda a documentação detalhada está em `/docs/pages/*.md`.

---

## 📘 Entedimento do Negócio e dos Dados

<details>
<summary>📊 Clique para Expandir</summary>

- [Entendimento do Negócio](docs/pages/entendimento_negocio.md)
- [Entendimento dos Dados](docs/pages/entendimento_dados.md)

</details>

---

## 🔎 Exploração dos Dados (EDA)

<details>
<summary>📊 Clique para Expandir</summary>

- [EDA Estatística Descritiva](docs/pages/eda_descritiva.md)
- [EDA Estatística Inferencial](docs/pages/eda_inferencial.md)

</details>

---

## 🛠 Feature Engineering

<details>
<summary>🛠 Clique para Expandir</summary>

- [Criação de variáveis derivadas](docs/pages/feature_engineering.md)

</details>

---

## ⚙️ Pré-processamento

<details>
<summary>⚙️ Clique para Expandir</summary>

- [Imputação e Limpeza](docs/pages/preprocessamento.md#imputacao)

</details>

---

## 🤖 Modelagem

<details>
<summary>🤖 Clique para Expandir</summary>

### Modelos, Threshold e Tuning
- [Regressão Logística](docs/pages/modelagem.md#logistic)  
- [Random Forest](docs/pages/modelagem.md#rf)  
- [Gradient Boosting](docs/pages/modelagem.md#gb)  
- [Threshold e Tuning](docs/pages/modelagem.md#gb) 

</details>

---

## 📏 Avaliação

<details>
<summary>📏 Clique para Expandir</summary>

- [Métricas: AUC, F1, Recall, Precision](docs/pages/04_modelagem.ipynb)
- [Matriz de confusão](docs/pages/04_modelagem.ipynb#cm)
- [Precision-Recall Curve](docs/pages/04_modelagem.ipynb#pr)

</details>

---

## 🚀 Deploy

<details>
<summary>🚀 Clique para Expandir</summary>

- [API (FastAPI)](docs/pages/deploy_api.md)
- [App (Streamlit/Gradio)](docs/pages/deploy_app.md)

</details>

---

## 📓 Notebooks Principais

- [00 — EDA Tratamento](notebooks/00_eda_tratamento.ipynb)  
- [01 — EDA Descritiva](notebooks/01_eda_descritiva.ipynb)  
- [02 — EDA Inferencial](notebooks/02_eda_inferencial.ipynb)  
- [03 — Pré-processamento](notebooks/03_preprocessing_pipeline.ipynb)  
- [04 — Modelagem](notebooks/04_modelagem.ipynb)  

---

## 📚 Estrutura do Projeto

```bash
ds-otif-detection-ml/
│
├── api/                  # API FastAPI
├── app/                  # Streamlit/Gradio
├── database/             # raw/interim/processed
├── deploy/               # Docker e Heroku
├── docs/                 # Documentação detalhada
├── models/               # Modelos treinados
├── notebooks/            # Notebooks principais
├── src/                  # Código modular
└── requirements.txt
````

---

## 🛠 Tecnologias Utilizadas

* Python 3.11
* Scikit-Learn
* Pandas / NumPy
* XGBoost / LightGBM
* SHAP
* FastAPI
* Streamlit / Gradio
* Docker
* Git / GitHub

---

## 🛠 requirements.txt
```txt
sqlalchemy 
pyodbc
pandas
numpy
scikit-learn
matplotlib
seaborn
xgboost
jupyter
```

## ▶️ Como Rodar o Projeto

### 1. Criar ambiente

```bash
python -m venv venv
source venv/bin/activate   # Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

### 2. Rodar API

```bash
uvicorn api.main:app --reload
```

### 3. Rodar App

```bash
streamlit run app/streamlit_app.py
```

---

## 🗺 Roadmap do Projeto

* ✔ Setup inicial
* ✔ Estrutura de documentação
* ✔ EDA completa
* 🔄 Pré-processamento
* 🔄 Modelagem
* 🔄 Avaliação
* 🔄 Deploy
* 🔄 Relatório final / apresentação

---

## 📬 Contato

**LinkedIn:** [Tiago Lima](https://www.linkedin.com/in/tiago-lima-935049154/)  
**GitHub:** [Tiago 466](https://github.com/tiago466)

---

<div align="left">
  <a href="#topo" title="Voltar ao início do README">⬆️ Topo</a>
</div>

---