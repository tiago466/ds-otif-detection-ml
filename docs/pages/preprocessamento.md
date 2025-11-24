# 03 - Pré-Processamento e Construção do Pipeline (scikit-learn)

<a href="../../README.md" title="Voltar para a página principal">
🏠 Voltar para Home
</a>

Este documento descreve **todas as etapas de pré-processamento** aplicadas ao dataset **acompanhamento_operacional_FE.csv**, conforme implementadas no notebook `03_preprocessing_pipeline.ipynb`.
O objetivo é garantir **qualidade, consistência, ausência de data leakage e reprodutibilidade total** para uso em modelos de Machine Learning.

---

## 🔧 **1. Carregamento do Dataset**

Carregamos o dataset processado após o EDA e Feature Engineering:

```
df = pd.read_csv("../database/processed/acompanhamento_operacional_FE.csv")
```

Esse arquivo já contém:

* Valores tratados (nulos resolvidos no EDA)
* Tipos ajustados
* Features criadas no arquivo FE (ex.: lead_time_total, complexidade_operacional, flags binárias)

---

## 🔎 **2. Identificação dos Tipos de Variáveis**

Separação correta entre **variáveis numéricas e categóricas**:

* **numéricas:** todas as `int64` e `float64`
* **categóricas:** todas as `object`

```
num_cols = df.select_dtypes(include=['int64','float64']).columns.tolist()
cat_cols = df.select_dtypes(include=['object']).columns.tolist()
```

▶️ **Por que isso é importante?**
Porque cada tipo de variável exige um tratamento diferente no pipeline (imputação, escala, codificação).

---

## 🧩 **3. Imputação de Valores Ausentes**

Mesmo após a limpeza inicial, garantimos **robustez** usando imputadores padronizados dentro do pipeline.

### ✔ Numéricas → *Mediana*

```
numeric_imputer = SimpleImputer(strategy="median")
```

**Motivo:**

* A mediana é robusta contra outliers
* Adequada para dados operacionais que têm caudas longas e valores extremos

### ✔ Categóricas → *Moda (most_frequent)*

```
categorical_imputer = SimpleImputer(strategy="most_frequent")
```

**Motivo:**

* Evita criar categorias artificiais
* Mantém consistência operacional
* Funciona muito bem com colunas como UF, modalidade, sigla_cliente etc.

---

## 🔄 **4. Codificação Categórica (Encoding)**

Utilizamos **OneHotEncoder**, que transforma cada categoria em uma coluna binária.

```
categorical_encoder = OneHotEncoder(
    handle_unknown="ignore",
    sparse_output=False
)
```

### Por que usar OneHot?

* Modelos clássicos (LogReg, RF, GBM) funcionam melhor com dados numéricos
* Evita atribuir pesos falsos (como ocorreria com Label Encoding)
* `handle_unknown="ignore"` evita erros em inferências reais

---

## 📏 **5. Escalonamento de Variáveis Numéricas (Scaling)**

Usamos **StandardScaler**, que transforma todas as features numéricas para:

* média = 0
* desvio padrão = 1

```
numeric_scaler = StandardScaler()
```

### Por que isso é importante?

* Modelos como **Regressão Logística** e **SVM** são sensíveis à escala
* Evita que features com grande magnitude dominem o modelo
* Melhora convergência e estabilidade matemática
* Mesmo Random Forest e Gradient Boosting, que não precisam de scaling, **não são prejudicados** pela padronização

---

## 🏗️ **6. Montagem do ColumnTransformer**

Aqui unimos todas as etapas anteriores em um bloco único que aplica automaticamente:

### Pipeline numérico:

* imputação (mediana)
* StandardScaler

### Pipeline categórico:

* imputação (moda)
* OneHotEncoder

```
preprocess = ColumnTransformer(transformers=[
    ("num_pipeline", Pipeline(steps=[
        ("imputer", numeric_imputer),
        ("scaler", numeric_scaler)
    ]), num_cols),

    ("cat_pipeline", Pipeline(steps=[
        ("imputer", categorical_imputer),
        ("encoder", categorical_encoder)
    ]), cat_cols)
])
```

📌 **Essa é a etapa que evita data leakage.**

Por quê?

➡ Tudo é aplicado *dentro do pipeline*,
➡ que só roda usando **apenas os dados de treino durante o fit**,
➡ garantindo que nenhuma informação dos dados de teste vaza para o treinamento.

---

## ✂️ **7. Split Train/Test**

Antes de treinar qualquer modelo:

```
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, stratify=y, random_state=42
)
```

### Cuidados importantes:

* **stratify=y** → preserva a proporção de atrasos/no atrasos
* **random_state=42** → garante reprodutibilidade total
* O split ocorre antes do `fit()` do pipeline → **evita vazamento total**

---

## 🔗 **8. Pipeline Final de Pré-Processamento**

Criamos um pipeline final reutilizável para qualquer modelo:

```
pipeline_preprocess = Pipeline(steps=[
    ("preprocess", preprocess)
])
```

### O que esse pipeline faz automaticamente?

Para cada coluna:

| Etapa     | Numéricas      | Categóricas |
| --------- | -------------- | ----------- |
| Imputação | Mediana        | Moda        |
| Escala    | StandardScaler | —           |
| Encoding  | —              | OneHot      |

➡ Tudo ocorre automaticamente durante o `.fit()` e `.transform()`
➡ Sem necessidade de mexer manualmente na base
➡ Zero risco de data leakage

---

# 📦 **Resumo Geral do Pré-Processamento**

### ✔ Correto para ML

### ✔ Escalável

### ✔ Reutilizável

### ✔ Blindado contra vazamento de dados

### ✔ Segue o padrão scikit-learn exigido em projetos profissionais

O pipeline está pronto para ser conectado diretamente ao notebook de modelagem (`04_modelagem.ipynb`), permitindo que modelos como:

* Logistic Regression
* Decision Tree
* Random Forest
* Gradient Boosting
* SMOTE Pipelines
* Class Weights

sejam treinados **com o mesmo processo padronizado e robusto**.
---

<div align="left">
  <a href="#topo" title="Voltar ao início do README">⬆️ Topo</a>
</div>

---