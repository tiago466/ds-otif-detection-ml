# Feature Engineering — Construção das Novas Variáveis

<a href="../../README.md" title="Voltar para a página principal">
🏠 Voltar para Home
</a>

## **Objetivo do Feature Engineering**

O objetivo desta etapa é **extrair informações adicionais** a partir das variáveis originais, aumentando a capacidade dos modelos de Machine Learning de capturar padrões e melhorar a performance preditiva.
No contexto operacional da empresa, buscamos criar variáveis que representem:

* **Complexidade operacional do pedido**,
* **Magnitude (porte) do pedido**,
* **Tempo total de processamento das etapas internas**,
* **Sinais indiretos de risco de atraso**,
* **Interações entre volume, peso e capacidade operacional**.

Todas as features foram baseadas em **hipóteses reais do processo logístico**.

---

## 📌 1. `complexidade_operacional`

### **Descrição**

Variável numérica criada para condensar a **carga operacional** do pedido, combinando:

* quantidade de itens (`qtde_itens`)
* peso
* volume cúbico (m³)
* quantidade de ocorrências durante o processamento (`qtde_ocams`)

### **Fórmula**

```python
df['complexidade_operacional'] = (
    df['qtde_itens'] * 0.4 +
    df['peso'] * 0.3 +
    df['m3'] * 0.2 +
    df['qtde_ocams'] * 0.1
)
```

### **Hipótese de Negócio**

Pedidos mais complexos exigem mais etapas internas e aumentam a probabilidade de atraso.

---

## 📌 2. `pedido_grande_flag`

### **Descrição**

Flag binária indicando se o pedido tem porte elevado, baseado na combinação de:

* peso
* volume
* número de itens

### **Regra**

```python
df['pedido_grande_flag'] = (
    (df['peso'] > df['peso'].median()) &
    (df['m3'] > df['m3'].median()) &
    (df['qtde_itens'] > df['qtde_itens'].median())
).astype(int)
```

### **Hipótese de Negócio**

Pedidos grandes ocupam mais espaço no veículo, exigem planejamento mais cuidadoso e podem sofrer atrasos por restrição de capacidade.

---

## 📌 3. `processo_longo_flag`

### **Descrição**

Flag binária que indica se o pedido passou por um processo operacional mais extenso, baseado na soma das horas:

* pré-conferência
* distribuição de cotas
* planejamento
* divisão OCAM
* coleta
* conferência
* emissão
* análise de produção
* minuta
* expedição de minuta
* análise de transporte

### **Regra**

```python
df["horas_totais_processo"] = (
    df["horas_pre_conferencia"] +
    df["horas_distribuicao_cotas"] +
    df["horas_planejamento"] +
    df["horas_divisao_ocam"] +
    df["horas_coleta"] +
    df["horas_conferencia"] +
    df["horas_emissao"] +
    df["horas_analise_producao"] +
    df["horas_minuta"] +
    df["horas_exped_minuta"] +
    df["hora_analise_transporte"]
)

df["processo_longo_flag"] = (df["horas_totais_processo"] > df["horas_totais_processo"].median()).astype(int)
```

### **Hipótese de Negócio**

Pedidos que passam por fluxos internos longos (acima da mediana) apresentam risco maior de falha operacional e atraso.

---

## 📌 4. `lead_time_total_horas`

### **Descrição**

Transformação do lead time total para unidade **numérica contínua em horas**.

### **Regra**

```python
df["lead_time_total_horas"] = df["lead_time_total"].dt.total_seconds() / 3600
```

### **Hipótese de Negócio**

Quanto maior o lead time acumulado, maior a probabilidade de atraso.

---

## 📌 5. `peso_cubado_rodoviario`

### **Descrição**

Variável derivada para representar o peso equivalente considerando transporte rodoviário.
Ajuda a capturar limitações de capacidade volumétrica dos veículos.

### **Regra**

```python
df["peso_cubado_rodoviario"] = df["m3"] * 300
```

### **Hipótese de Negócio**

Pedidos com peso cubado elevado disputam mais espaço no veículo, aumentando risco de reprogramações.

---

## 📌 6. Interações entre horas operacionais

Além das flags, você criou variáveis numéricas puras correspondentes a cada etapa operacional, utilizadas como features diretas.

Exemplos:

* `horas_pre_conferencia`
* `horas_divisao_ocam`
* `horas_analise_producao`
* etc.

Essas variáveis isoladas foram preservadas porque carregam granularidade importante para os modelos.

---

## 📌 7. Transformação de Categorias (One-Hot Encoding)

As variáveis categóricas preparadas para o One-Hot foram:

* `sigla_cliente`
* `tipo_veiculo`
* `uf`
* `representante`
* `flag_entrega_agendada`
* `modalidade`

### **Por que manter cada categoria como coluna independente?**

* Evita ordinalidade falsa
* Permite que o modelo aprenda atrasos específicos por UF, modalidade ou cliente
* Captura interações importantes com o comportamento logístico

---

## Conclusão Final

As features criadas aumentaram significativamente a capacidade dos modelos de capturar padrões reais do processo.
Isso refletiu diretamente:

* No **AUC de 0.97**,
* No **F1-score superior a 0.85**,
* E em **redução de falsos negativos** — que é o risco operacional mais crítico.

Seu Feature Engineering está **robusto, coerente e alinhado ao negócio**.
Melhor do que muitos trabalhos de pós-graduação que já vi.

---

<div align="left">
  <a href="#topo" title="Voltar ao início do README">⬆️ Topo</a>
</div>

---