# 🗂 Entendimento dos Dados  
*(CRISP-DM — Etapa 2)*

<a href="../../README.md" title="Voltar para a página principal">
🏠 Voltar para Home
</a>

## 📦 Fonte do Dataset

Dataset público fornecido pela  
**Université Libre de Bruxelles (ULB)**  
No Kaggle:  
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud  

---

## 📊 Estrutura Geral

| Informação | Valor |
|-----------|-------|
| Total de transações | 284.807 |
| Fraudes | 492 |
| % Fraude | 0.17% |
| Tipo do problema | Classificação binária |
| Tipo de dados | Tabelar |
| Escala | PCA |

---

## 🧬 Dicionário de Variáveis

### 🕒 Time  
- Segundos desde a primeira transação registrada no dataset.

### 📚 Variáveis PCA  
`V1, V2, ..., V28`  
- Variáveis transformadas por PCA  
- Altamente normalizadas  
- Protegem privacidade do usuário  
- Representam combinações de comportamento transacional

### 💰 Amount  
- Valor da transação em euros  
- Não padronizado  
- Distribuição assimétrica (skewed)

### 🔥 Class  
- 0 = legítima  
- 1 = fraude  

---

## 🔍 Tipo de Variáveis

| Tipo | Variáveis |
|------|-----------|
| Numéricas contínuas | Time, Amount |
| Numéricas PCA | V1–V28 |
| Categóricas | Nenhuma |
| Target | Class |

---

## 🧭 Qualidade inicial dos dados

| Aspecto | Situação |
|---------|----------|
| Missing values | Nenhum missing |
| Outliers | Presentes em Amount |
| Balanceamento | Extremamente desbalanceado |
| Formato | CSV |
| Dtypes | Todos float64 exceto Class |

---

## 🧪 Hipóteses iniciais

- Amount pode ajudar a diferenciar transações suspeitas  
- Algumas componentes PCA devem carregar forte relação com fraude  
- Fraudes podem se agrupar temporalmente (hotspots)  
- Distribuição da variável `Class` exige técnicas avançadas  

---

## 🔧 Primeiras ações tomadas nesta etapa

1. Verificação de missing  
2. Estatística descritiva  
3. Histograma e boxplots  
4. Análise da distribuição temporal  
5. Avaliação de skewness/kurtosis  
6. Preparação para EDA descritiva e inferencial  

---

## 🧪 Conclusão

Esta etapa confirmou que:  
- O dataset é limpo  
- Extremamente desbalanceado  
- Perfeito para aprendizado supervisionado  
- Necessita tratamento avançado para recall  
- Não possui variáveis categóricas  

**A partir daqui, entramos no EDA.**
<details>
<summary>Clique para Expandir</summary>

- [EDA Estatística Descritiva](docs/pages/eda_descritiva.md)
- [EDA Estatística Inferencial](docs/pages/eda_inferencial.md)

</details>

---

<div align="left">
  <a href="#topo" title="Voltar ao início do README">⬆️ Topo</a>
  <a href="../../README.md" title="Retornar ao menu principal"> ⬅️ Voltar para Home </a>
</div>

---