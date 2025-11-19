# 🧩 Entendimento do Negócio  
*(CRISP-DM — Etapa 1)*

<a href="../../README.md" title="Voltar para a página principal">
🏠 Voltar para Home
</a>

# 🎯 1. Objetivo do Projeto

Construir um sistema preditivo capaz de:
 - Determinar se um pedido será No Prazo ou Fora do Prazo
 - Prever possíveis atrasos ainda durante as etapas internas (I, S, E, Q, W etc.)
 - Aumentar o OTIF da Zenatur e reduzir prejuízos contratuais
 - Gerar recomendações operacionais preventivas

---

# 🔍 Contexto Operacional

A Zenatur é responsável por operações de transporte e distribuição para grandes clientes (VRA, JNJ, NES etc.).
A performance de entrega é medida pelo KPI OTIF (On Time In Full).

## 🚚 Mas o que é OTIF?

**OTIF (On Time In Full)** é o principal indicador de qualidade logística.

Ele mede:
 - **On Time (No Prazo):** A entrega ocorreu dentro do prazo combinado?
 - **In Full (Completo):** O pedido foi entregue com todos os itens corretos e sem avarias?

> Neste projeto trabalhamos apenas com a previsão de **On Time In Full**.

Quando OTIF cai:
 - contratos são impactados
 - multas são aplicadas
 - há desgaste com clientes-chave
 - operação tem que acionar “modos de emergência” para compensar atrasos

---

# 🔥 3. Dor do Negócio

A Zenatur pode enfrentar:
 - **Prejuízo Reputacional** devido aos atrasos constantes fragilizando as relações comerciais.
 - **Prejuízos Contratuais** como multas, glosas e cláusulas de OTIF mínimo (90%–95%).
 - **Prejuízos Operacionais** como:
    > * Mudança não planejada de modalidade (rodoviário → aéreo).
    > * Hora extra.
    > * Reprocesso de documentação.
    > * Contratação emergencial de transportadoras.
 - **Perda de Produtividade** ao gasto de tempo operacional apagando incêndios ao invés de agir preventivamente.
 - **Falta de Visibilidade**, pois hoje o risco de atraso é percebido **apenas quando já está tarde demais**.

---

# 🎯 4. O que o Software Precisa Fazer

## 4.1. Predição de Atraso

```
Entrada → parâmetros do pedido
Saída → previsão: No Prazo / Fora do Prazo
```

## 4.2. Previsão de Data de Expedição

Baseada nos SLAs das etapas anteriores.

## 4.3. Recomendações Inteligentes

Se risco elevado:

* “Verificar pendências na emissão.”
* “Acompanhar etapa de conferência.”
* “Planejar coleta antecipada.”

## 4.4. Painel Operacional

Exemplo:

| Cliente | Pedido | Etapa Atual | Data Solicitação | Status            | Recomendação    |
| ------- | ------ | ----------- | ---------------- | ----------------- | --------------- |
| PEG     | 324563 | E           | 10/11/25         | 🔴 Risco iminente | Acionar Emissão |
| PEG     | 324566 | I           | 14/11/25         | 🟢 No Prazo       | Acompanhar      |
| NTL     | 324565 | S           | 14/11/25         | 🟡 Risco Moderado | Validar Coleta  |

---

# 🧠 5. Definição do Problema em ML

### Tipo do problema

**Classificação binária**

* 1 → atrasado
* 0 → no prazo

### Target (variável resposta)

```
atraso_final = data_entrega > dt_prazo_limite_cliente
```

### Momento da previsão

Logo após a etapa de **planejamento** (`dt_planeja`).

### Por que esse momento?

* Etapa ainda controlável
* Dados suficientes
* Ação ainda possível

---

# 🔮 6. Métricas do Modelo

* **Recall da classe atraso** (o mais importante)
* Precision
* F1-score
* Matriz de confusão
* ROC-AUC

---

# 🚫 7. Restrições do Problema

* Muitos campos nulos
* Diferenças grandes entre clientes (VRA, COL, JNJ, NTL…)
* SLAs variam por região, modalidade e operação
* Erros impactam diretamente contratos
* Feature leakage se usar etapas futuras indevidamente

---

# 📌 8. Conclusão

Prever atrasos **antes que aconteçam** permite:

* Redução de custos
* Cumprimento contratual
* Aumento do OTIF
* Maior satisfação do cliente
* Operações mais inteligentes e proativas

Este documento define a visão estratégica que guia todas as próximas etapas do pipeline CRISP-DM.

---

<div align="left">
  <a href="#topo" title="Voltar ao início">⬆️ Topo</a>
  <a href="../../README.md" title="Retornar ao menu principal"> ⬅️ Voltar para Home </a>
</div>