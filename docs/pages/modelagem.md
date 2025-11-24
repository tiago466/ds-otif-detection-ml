# 04 - Modelagem

<a href="../../README.md" title="Voltar para a página principal">
🏠 Voltar para Home
</a>

## 🎯 Visão Geral

Este notebook marca o início da fase de **modelagem preditiva**, utilizando modelos clássicos de Machine Learning para estabelecer um baseline sólido antes de avançar para algoritmos mais sofisticados.

Aqui começamos a responder à pergunta central do projeto:

> **“Com base nas informações operacionais, conseguimos prever se um pedido irá atrasar (fl_atraso_cli)?”**

Para isso, utilizamos os dados já tratados e enriquecidos (Feature Engineering) nos notebooks anteriores:

- `00_eda_tratamento.ipynb`  
- `01_eda_descritiva.ipynb`  
- `02_eda_inferencial.ipynb`  
- `03_preprocessing_pipeline.ipynb`  

---

## 📌 Objetivos deste Notebook

Este notebook implementa:

1. **Modelo Baseline (DummyClassifier)**  
   - estabelece uma linha de comparação mínima para avaliar se os modelos realmente têm poder preditivo.

2. **Modelos Clássicos de Classificação**
   - **Regressão Logística**  
   - **Árvore de Decisão (Decision Tree Classifier)**  

3. **Integração com o Pipeline de Pré-processamento**  
   - garante que imputação, codificação e escala sejam aplicadas corretamente dentro de cada modelo.

4. **Validação e Métricas**
   - Accuracy
   - Precision
   - Recall
   - F1-score
   - ROC AUC
   - Classification Report
   - Matriz de Confusão

5. **Comparação entre modelos**
   - para selecionar o melhor candidato a ser refinado no notebook 05 (modelos avançados).

## 📊 Métricas de Avaliação de Modelos de Classificação

### (Accuracy, Precision, Recall, F1-Score, ROC AUC)

Ao avaliar modelos de Machine Learning para **classificação**, utilizamos métricas que medem diferentes aspectos da performance — cada uma adequada para um tipo de problema e custo de erro.

Abaixo segue a explicação **detalhada, profissional e didática**, para você colocar diretamente no arquivo **modelagem.md**.

---

## 1. Acurácia (Accuracy)

### 📌 **O que mede**

A proporção de todas as previsões corretas:

[
\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}
]

### 📌 **Quando usar**

* Quando as classes estão **balanceadas**.
* Quando **todos os erros têm o mesmo custo**.

### 📌 **Como interpretar**

* Valores próximos de **1.0** → excelente desempenho.
* Pode ser **enganosa em dados desbalanceados**.

**Exemplo**:
Se apenas 10% dos pedidos atrasam, um modelo que sempre diz “não vai atrasar” tem 90% de acurácia — mas é inútil.

---

## 2. Precisão (Precision)

### 📌 **O que mede**

Entre todas as previsões **positivas**, quantas estavam realmente corretas?

[
\text{Precision} = \frac{TP}{TP + FP}
]

### 📌 **Quando usar**

* Quando o custo de um **falso positivo** é alto.
* Exemplos:

  * Diagnóstico de doenças graves com exames caros.
  * Detecção de fraude (alertas falsos têm custo).
  * OTIF: avisar atraso quando não há atraso → gera ruído operacional.

### 📌 **Como interpretar**

* Alta precisão = o modelo quase não “aluga” falso alarme.

---

## 3. Recall (Sensibilidade)

### 📌 **O que mede**

Entre todos os casos positivos reais, quantos o modelo identificou?

[
\text{Recall} = \frac{TP}{TP + FN}
]

### 📌 **Quando usar**

* Quando o custo de um **falso negativo** é muito alto.
* Exemplos:

  * Perder uma fraude
  * Perder paciente realmente doente
  * No OTIF: perder um atraso real é **muito pior** que dizer que vai atrasar à toa

### 📌 **Como interpretar**

* Alto recall = o modelo consegue capturar a maioria dos atrasos reais.

---

## 4. F1-Score

### 📌 **O que mede**

A média harmônica entre **precisão** e **recall**:

[
\text{F1} = 2 \cdot \frac{Precision \cdot Recall}{Precision + Recall}
]

### 📌 **Quando usar**

* Quando você quer **uma única métrica equilibrada** entre precisão e recall.
* Quando o dataset é **desbalanceado**.
* Quando você quer comparar modelos de forma justa.

### 📌 **Como interpretar**

* F1 alto = modelo equilibrado
* F1 baixo = modelo falha em precisão, recall ou ambos

---

## 5. AUC ROC (Área sob a Curva ROC)

### 📌 **O que mede**

Avalia a capacidade do modelo de separar classes **em todos os thresholds possíveis**.

[
0.5 = \text{modelo aleatório} \
1.0 = \text{separação perfeita}
]

### 📌 **Quando usar**

* Avaliação geral do modelo.
* Comparação entre modelos.
* Ótimo para visualizar qualidade da separação.

### 📌 **Limitações**

* Pode ser otimista em datasets extremamente desbalanceados.
* Menos intuitiva para explicar ao time de negócio em comparação ao Precision/Recall.

---

## 🎯 Resumo Profissional das Métricas

| Métrica       | O que mede                         | Quando usar                 | Risco                        |
| ------------- | ---------------------------------- | --------------------------- | ---------------------------- |
| **Accuracy**  | % de previsões corretas            | Classes balanceadas         | Enganosa em desbalanceamento |
| **Precision** | Confiabilidade dos positivos       | Falso positivo custa caro   | Baixa pode gerar ruído       |
| **Recall**    | % de positivos capturados          | Falso negativo custa caro   | Alta pode reduzir precisão   |
| **F1**        | Equilíbrio entre Precisão e Recall | Comparação justa de modelos | Pode esconder detalhes       |
| **ROC AUC**   | Separação geral das classes        | Comparar modelos            | Otimista em desbalanceamento |

---

## Como se relacionam

* **Precision ↑** → menos falsos positivos
* **Recall ↑** → menos falsos negativos
* **F1 alto** → bom equilíbrio
* **ROC AUC alto** → maior separabilidade estrutural

No seu projeto OTIF:

📌 **Recall é extremamente importante** — pois perder atrasos reais seria devastador.
📌 **Precision também é importante** — mas secundário.
📌 **F1 resume a performance.**
📌 **ROC AUC confirma a capacidade estrutural do modelo.**

## Modelos

### Modelo Baseline - DummyClassifier

**Descrição:** O modelo baseline tem como objetivo estabelecer um ponto de referência mínimo para comparação dos modelos reais.
Neste trabalho, será utilizado o DummyClassifier(strategy="most_frequent"), que sempre prevê a classe majoritária encontrada no dataset.

#### **Nota Técnica:** 

Esses valores são esperados, já que o modelo nunca prevê “1 = atraso”, apenas repete a classe dominante (0).
O comportamento demonstra, viés extremo para a classe majoritária, incapacidade total de detectar atrasos e desempenho equivalente a uma classificação aleatória (ROC AUC = 0.5)

**Importância do Baseline:** A função do baseline não é prever corretamente, mas sim, estabelecer o ponto mínimo aceitável de desempenho, garantir que um modelo real não seja pior do que adivinhar sempre “não atraso”, servir como referência para medir ganho de performance e deixar explícito o impacto do desbalanceamento da classe alvo.

**Conclusão**

O baseline confirma que o dataset possui forte desbalanceamento, então métricas como precision, recall e F1 serão fundamentais, com isso é provável que qualquer modelo útil deve superar esse resultado, principalmente em recall para a classe "1" (atraso)

Assim, os modelos seguintes devem ser avaliados não apenas por accuracy, mas também por F1, Recall e ROC AUC, que de fato capturam a qualidade da detecção de atrasos.

### Treinando a Regressão Logística (LogisticRegression)

**Descrição:** A regressão logística é uma técnica estatística para prever a probabilidade de um evento ocorrer, com base em variáveis independentes.

#### **Nota Técnica:** 
A Regressão Logística apresentou excelente desempenho no problema de classificação de atraso (OTIF), especialmente ao considerar o desbalanceamento natural da base.

**Principais métricas obtidas:**

- **Accuracy:** 0.7082
- **Precision:** 0.4728
- **Recall:** 0.7279
- **F1 Score:** 0.5732
- **ROC AUC:** 0.7879

**Interpretação:**
- **O recall de 72%** significa que o modelo identifica a maior parte dos pedidos atrasados, característica fundamental em cenários logísticos.
- **A precision de 47%**, em bases desbalanceadas, é extremamente elevada e indica bom poder discriminativo.
- **O F1 Score acima de 57%** mostra bom equilíbrio entre precisão e recall.
- **O ROC AUC de 79%** evidencia capacidade preditiva robusta, muito acima do esperado para um modelo linear.

**Conclusão**
A Regressão Logística estabeleceu um baseline forte, mostrando que o processo de pré-processamento e as features derivadas capturam bem o comportamento operacional dos atrasos.
Este modelo servirá como referência para avaliar técnicas mais avançadas, como Random Forest, Gradient Boosting e XGBoost.

### 5. Árvore de Decisão (DecisionTreeClassifier)

**Descrição:** Uma DecisionTreeClassifier é um modelo de aprendizado supervisionado que usa uma estrutura de árvore para fazer previsões. É usada para classificação e funciona como um fluxograma de regras de decisão, onde cada nó representa um teste de atributo, cada ramo é o resultado do teste e os nós-folha representam a classe final ou a previsão.

#### **Nota Técnica:** 
A Árvore de Decisão apresentou um desempenho surpreendentemente robusto no problema de classificação de atrasos logísticos, alcançando:

- **Accuracy:** 0.893
- **Precision:** 0.779
- **Recall:** 0.840
- **F1 Score:** 0.809
- **ROC AUC:** 0.896

Esses resultados indicam equilíbrio entre a capacidade de identificar atrasos (recall) e evitar alarmes falsos (precision).  

O modelo capturou com sucesso padrões operacionais estruturais, muito influenciados pelas novas features de engenharia criadas no EDA inferencial, em especial o lead_time_total_horas, complexidade_operacional e pedido_grande_flag.

O uso de class_weight="balanced" aliado ao pipeline completo de pré-processamento contribuiu significativamente para reduzir viés e estabilizar a performance do modelo.

Os resultados superam amplamente o baseline e já se aproximam de modelos ensemble como Random Forest ou Gradient Boosting, indicando forte separabilidade inerente aos dados.

### 6. Random Forest Classifier (RandomForestClassifier)

**Descrição:** Random Forest é um algoritmo de aprendizado de máquina que combina múltiplas árvores de decisão para melhorar a precisão e a estabilidade das previsões. Ele funciona treinando cada árvore em diferentes partes aleatórias dos dados e depois combinando os resultados por votação (para classificação) ou média (para regressão). Esse método ajuda a reduzir o risco de overfitting (quando o modelo se ajusta demais aos dados de treinamento) e é amplamente usado tanto para tarefas de classificação quanto de regressão. 

#### **Nota Técnica:** 
O modelo Random Forest apresentou desempenho superior na maior parte das métricas relevantes para o problema de previsão de atrasos operacionais. Com um ROC AUC de 0.9576, o modelo demonstrou excelente capacidade de separação entre pedidos atrasados e entregues no prazo.

O recall de 0.9093 foi o maior entre os modelos testados, indicando que o Random Forest é o mais eficaz em identificar pedidos que irão atrasar, a característica mais importante no contexto logístico, onde falsos negativos (atrasos não detectados) são extremamente prejudiciais.

Embora o accuracy (0.8839) seja levemente inferior ao Decision Tree, o modelo compensou com uma maior sensibilidade e com uma robustez significativamente maior na generalização. O F1 Score de 0.8084 reforça o equilíbrio entre precisão e recall.

O comportamento do Random Forest também é mais estável, reduzindo riscos de overfitting quando comparado à árvore de decisão individual. A combinação de desempenho forte, robustez estatística e alta capacidade de separação coloca o Random Forest como o modelo mais consistente do conjunto até o momento.

### 7. Gradient Boosting (GradientBoostingClassifier)

**Descrição:** Gradient Boosting é um algoritmo de aprendizado de máquina que cria um modelo forte e preciso combinando vários modelos mais fracos (geralmente árvores de decisão) sequencialmente. Cada modelo subsequente foca em corrigir os erros cometidos pelo modelo anterior, minimizando uma função de perda (o erro) por meio de um processo iterativo que usa o gradiente para guiar as melhorias. É amplamente utilizado em tarefas de classificação e regressão.

#### **Nota Técnica:** 
O Gradient Boosting é um algoritmo de ensemble baseado na construção sequencial de árvores fracas, onde cada nova árvore tenta corrigir os erros da árvore anterior.
Em muitos cenários, esse modelo supera técnicas como Random Forest e Decision Tree, especialmente quando os padrões são sutis e os dados têm pouco ruído.

No entanto, seu desempenho depende fortemente da natureza da base. Em contextos logísticos, caracterizados por alta variabilidade, caudas pesadas e outliers, o GBM tende a perder estabilidade.

---

## **3. Resultados Obtidos**

| Métrica       | Valor  |
| ------------- | ------ |
| **Accuracy**  | 0.8191 |
| **Precision** | 0.7681 |
| **Recall**    | 0.4699 |
| **F1-score**  | 0.5831 |
| **ROC AUC**   | 0.8838 |

---

## **4. Interpretação dos Resultados**

### **4.1 Pontos fortes**

* **Boa precision (76%)**: quando o modelo prevê atraso, ele acerta muitas vezes.
* **Bom AUC (0.88)**: indica uma capacidade razoável de discriminar entre atrasos e não atrasos.

---

### **4.2 Pontos fracos (críticos)**

O principal problema está no **Recall = 46%**, o mais baixo entre todos os modelos avaliados.

**Recall baixo significa:**

> O modelo não identifica grande parte dos pedidos que realmente atrasam.

Em problemas logísticos **isso é inaceitável**.
A empresa precisa **prever atrasos reais**, mesmo que isso gere alguns falsos positivos.
O custo de um atraso real não previsto é muito maior do que o custo de prever atraso quando não existe.

Assim, apesar de algumas métricas satisfatórias, o modelo apresenta uma **falha estrutural no objetivo de negócio**.

---

### **4.3 Comparação com outros modelos**

O Gradient Boosting se mostrou **inferior ao Random Forest e à Decision Tree** em métricas essenciais:

#### ✔ Random Forest

* Recall: **0.9093**
* F1: **0.8084**
* ROC AUC: **0.9576**

#### ✔ Decision Tree

* Recall: **0.8407**
* F1: **0.8092**

#### ✘ Gradient Boosting

* Recall: **0.4699**
* F1: **0.5831**

**Conclusão:**

> Apesar de tecnicamente robusto, o Gradient Boosting não se ajustou bem ao comportamento da base, perdendo desempenho nas métricas mais relevantes para o problema.

---

## **5. Conclusão Técnica**

O Gradient Boosting apresentou resultados sólidos em algumas métricas, mas mostrou **desempenho insuficiente para o objetivo operacional**, deixando escapar grande parte dos atrasos reais.

Por esse motivo:

### **O modelo NÃO é adequado como candidato final.**

### Os modelos **Random Forest** e **Decision Tree** apresentam performance superior e maior aderência ao objetivo do negócio.

## 8. Comparando os Melhores Modelos

O melhor modelo global foi o Random Forest, porque ele entrega o melhor balanço entre precisão, recall, estabilidade e capacidade preditiva real.

**Por que NÃO escolhemos o Decision Tree, apesar da accuracy maior?**
O Decision Tree apresentou accuracy ligeiramente maior (0.8932), mas isso foi artificial, pois é muito provavel que tenha sofrido overfitting, porque árvores singulares tendem a memorizar o dataset e o ROC AUC dele (0.8956) é bem inferior ao do Random Forest (0.9576), mostrando que sua capacidade de generalização é menor.

**Por que NÃO escolhemos Gradient Boosting?**
Ele teve desempenho bom em precisão, mas recall extremamente baixo (0.47).
Para um problema de operação logística, perder atrasos reais é inaceitável então recall é crucial.

**Por que NÃO escolhemos Regressão Logística?**
É um modelo simples, baseline, e serviu para confirmar que modelos lineares não capturam bem a complexidade do processo logístico.

O Random Forest apresentou o melhor trade-off entre precisão, recall e capacidade de generalização, com o maior ROC AUC entre todos os modelos. Isso indica que ele distingue muito bem atrasos de não atrasos e por isso, ele foi selecionado como modelo final para otimizações e análise de threshold.

### 9. Tratamento de Desbalanceamento (Class Weights e SMOTE)

Modelos treinados sem compensação tendem a priorizar a classe majoritária, então, para mitigar isso, três técnicas foram avaliadas:

---

**4.1 — Class Weights (Regressão Logística)**

O class_weight="balanced" ajusta o peso das classes automaticamente, penalizando mais os erros na classe minoritária.  
O resultado aumenta sensivelmente o *recall*, mas mantém *precision* baixa, típico de modelos lineares.  
É um baseline válido, porém inferior aos modelos baseados em árvores.

---

**4.2 — SMOTE + Random Forest (Oversampling)**

SMOTE cria amostras sintéticas da classe minoritária, equilibra o dataset e melhora o aprendizado do modelo.  
O Random Forest treinado após o oversampling apresentou:

- **Accuracy:** 92,11%  
- **Precision:** 84,63%  
- **Recall:** 86,40%  
- **F1:** 85,50%  
- **ROC AUC:** 0,9704  

Este foi o melhor desempenho entre todos os modelos testados.
O SMOTE reduziu o viés da classe majoritária sem causar overfitting e permitiu que o Random Forest aprendesse padrões mais refinados sobre atrasos.

---

**4.3 — Random UnderSampling**

Reduz o número de exemplos da classe majoritária.
O recall aumentou fortemente (94%), mas houve queda na precision (72%), indicando aumento de falsos positivos.  
Foi útil como comparação, porém inferior ao modelo SMOTE + Random Forest.

---

**Conclusão Técnica**

O modelo **Random Forest + SMOTE** apresentou o melhor equilíbrio entre precisão, recall e separabilidade (AUC).  
Este modelo será utilizado como referência para as próximas etapas de otimização de threshold e interpretabilidade.

### 10. Thresholds de Decisão

## Nota Técnica

### **1. O que é o Threshold?**

Modelos de classificação binária como Random Forest, Logistic Regression e Gradient Boosting **não predizem diretamente classes**.
Eles predizem **probabilidades**.

Exemplo:

```
Probabilidade de atraso = 0.73 → modelo acha 73% de chance de atrasar
```

Para converter essa probabilidade em uma decisão **(0 = no prazo / 1 = atraso)**, usamos um **threshold (limiar)**.

O threshold padrão é **0.50**, mas ele **não é necessariamente o melhor ponto** para o negócio.

---

### **2. Por que variar o Threshold?**

Porque alterar o threshold muda o equilíbrio entre:

* **Precision** → quão corretas são as previsões de atraso
* **Recall** → quantos atrasos reais o modelo consegue detectar
* **F1-score** → equilíbrio entre os dois

**Threshold baixo (ex.: 0.10)**

* Recall altíssimo (detecta quase todos atrasos)
* Precision baixa (gera muitos falsos alarmes)

**Threshold alto (ex.: 0.85)**

* Precision altíssima (quando alerta, é certeiro)
* Recall muito baixo (quase não detecta atrasos)

---

### **3. Como realizamos a análise**

Testamos thresholds de **0.10 a 0.90**, e para cada valor calculamos:

* Precision
* Recall
* F1-score

Geramos tanto:

* uma **tabela comparativa dos thresholds**,
* quanto o **gráfico das curvas Precision × Recall × F1**.

Esses dois artefatos confirmaram o comportamento clássico esperado:

- Precision sobe conforme threshold aumenta
- Recall cai conforme threshold aumenta
- F1 tem um **pico** — esse é o threshold ideal

---

### **4. Resultado da Análise**

Tabela (trecho mais relevante):

| threshold | precision | recall    | f1        |
| --------- | --------- | --------- | --------- |
| 0.30      | 0.691     | 0.960     | 0.804     |
| 0.40      | 0.774     | 0.925     | 0.843     |
| **0.50**  | **0.846** | **0.863** | **0.855** |
| 0.60      | 0.904     | 0.768     | 0.831     |
| 0.70      | 0.946     | 0.635     | 0.760     |

O **melhor F1-score (0.855)** ocorreu exatamente no threshold **0.50**.

---

### **5. Conclusão da Otimização**

**O threshold ótimo para este problema é 0.50**, pois:

* mantém **alta capacidade de captura dos atrasos reais (recall = 0.863)**
* mantém **boa precisão (precision = 0.846)**
* e atinge o **maior F1-score entre todos os thresholds testados**

Ou seja, **é o ponto de equilíbrio ideal entre sensibilidade e precisão**, maximizando o desempenho global do modelo.

---

### **6. Justificativa para o negócio**

> *“No contexto operacional da logística, perder atrasos reais tem alto custo. Por isso, o threshold escolhido privilegia um balanço entre alertas corretos (precision) e detecção de atrasos reais (recall). O threshold de 0.50 foi selecionado por maximizar o F1-score e garantir o melhor equilíbrio operacional.”*

---

### **7. Conclusão final da nota técnica**

A análise de threshold demonstrou que o desempenho do modelo pode ser significativamente ajustado ao cenário real de operação. O threshold **não é um valor fixo**, mas sim um **parâmetro estratégico** que deve ser calibrado conforme:

* custos de erro,
* prioridades do negócio,
* e comportamento real dos dados.

Neste trabalho, o threshold de **0.50** foi comprovadamente o valor que **maximiza o desempenho preditivo** e **melhor atende ao contexto da Zenatur**.

---

<div align="left">
  <a href="#topo" title="Voltar ao início do README">⬆️ Topo</a>
</div>

---
