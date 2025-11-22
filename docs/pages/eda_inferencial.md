# EDA – Estatística Inferencial

<a href="../../README.md" title="Voltar para a página principal">
🏠 Voltar para Home
</a>

---

## **Visão Geral**

A Estatística Inferencial tem como objetivo compreender **relações causais e associativas** entre variáveis, testar hipóteses e investigar se diferenças observadas nos dados podem ser generalizadas para todo o processo operacional.

No contexto deste estudo sobre atraso logístico (OTIF), as análises inferenciais buscam responder:

- **Quais variáveis mais se relacionam com o atraso?**
- **Quais etapas impactam mais a probabilidade de um pedido atrasar?**
- **Existem diferenças estatisticamente significativas entre pedidos atrasados e não atrasados?**
- **Variáveis categóricas influenciam o atraso?**
- **As features numéricas mostram comportamento distinto entre os grupos 0/1 (no prazo / atraso)?**

Estas análises são essenciais para orientar no **Feature Engineering**, **Modelagem de Classificação** e **Interpretação de Resultados**.

---

# **1. Correlação (Pearson & Spearman)**

## ✔ Objetivo

Medir o grau de associação entre variáveis numéricas e o alvo (`fl_atraso_cli`), usando dois métodos:

- **Pearson** → relações lineares
- **Spearman** → relações monotônicas (mais robusto contra outliers e distribuições distorcidas)

---

## ✔ Principais Conclusões

### **1.1. Correlação de Pearson – Associações fracas (< 0.2)**

Top 5:

| Variável           | Correlação |
| ------------------ | ---------- |
| horas_divisao_ocam | **0.108**  |
| horas_planejamento | **0.101**  |
| horas_conferencia  | 0.085      |
| horas_coleta       | 0.082      |
| qtde_itens         | 0.059      |

> **Pearson mostrou correlações baixas**, o que é esperado para processos operacionais sujeitos a grande variabilidade e outliers.

---

### **1.2. Correlação de Spearman – Relações monotônicas moderadas (~0.20)**

| Variável               | Correlação |
| ---------------------- | ---------- |
| m3                     | **0.202**  |
| peso_cubado_rodoviario | **0.196**  |
| horas_minuta           | **0.194**  |
| peso                   | 0.167      |
| volume                 | 0.158      |
| horas_coleta           | 0.142      |
| horas_divisao_ocam     | 0.137      |

> Spearman capturou mais padrões, revelando que **pedidos maiores = maior risco de atraso**.

---

## ✔ Interpretação Técnica

* Correlações abaixo de **0.3** são comuns em dados reais de operações.
* Mesmo correlações fracas podem ser **altamente relevantes para modelos não lineares** (árvores, boosting).
* Spearman destacou que o atraso cresce de forma monotônica com o tamanho/complexidade do pedido.

---

# **2. ANOVA – Comparação de Médias (Atraso vs Não Atraso)**

## ✔ Objetivo

Testar se pedidos atrasados possuem **médias estatisticamente diferentes** das etapas operacionais.

* **H₀:** Não há diferença entre as médias dos grupos
* **H₁:** Há diferença significativa

Usamos **p-valor < 0.05** para rejeitar H₀.

---

## ✔ Resultados

Quase todas as variáveis numéricas apresentaram **diferenças altamente significativas**, incluindo:

| Variável           | F-statistic | p-valor |
| ------------------ | ----------- | ------- |
| horas_divisao_ocam | **5783.2**  | 0.000   |
| horas_planejamento | **5037.6**  | 0.000   |
| horas_conferencia  | **3564.7**  | 0.000   |
| horas_coleta       | **3330.8**  | 0.000   |
| m3                 | 1113.8      | 0.000   |
| peso               | 582.8       | 0.000   |

Variáveis **não significativas**:

* **volume**
* **horas_distribuicao_cotas**
* **hora_analise_transporte**

---

## ✔ Interpretação

* O F-statistic indica **quão forte é a separação** das médias entre os grupos.
* P-valores praticamente zero mostram que **as etapas operacionais têm comportamento bem diferente entre atrasos e não atrasos**.
* Reforça a ideia de que **complexidade operacional e duração das etapas** são determinantes para o OTIF.

---

# **3. Qui-Quadrado – Dependência de Variáveis Categóricas**

## ✔ Objetivo

Avaliar se categorias específicas (cliente, UF, modalidade, tipo do veículo etc.) têm associação com o atraso.

Testamos a independência entre:

* **sigla_cliente**
* **uf**
* **modalidade**
* **tipo_veiculo**
* **flag_entrega_agendada**

---

## ✔ Resultado

| Variável              | χ²        | p-valor | Significativo? |
| --------------------- | --------- | ------- | -------------- |
| sigla_cliente         | **38457** | 0.000   | ✔              |
| tipo_veiculo          | **49719** | 0.000   | ✔              |
| modalidade            | **40397** | 0.000   | ✔              |
| uf                    | **6800**  | 0.000   | ✔              |
| flag_entrega_agendada | 1231      | 0.000   | ✔              |

---

## ✔ Interpretação

* Todas as variáveis categóricas testadas são **dependentes do atraso**.
* Clientes, UF e modalidade possuem grande impacto no OTIF.
* Isso indica:

  * **localização**
  * **perfil de operação**
  * **tipo de transporte**

contribuem de forma importante para o risco de atraso.

---

# **4. Separabilidade – Atraso vs Não Atraso**

## ✔ Objetivo

Comparar **médias** entre os grupos e calcular:

* diferença relativa (%)
* **Cohen’s d** (tamanho do efeito)

---

## ✔ Resultados

As variáveis mais impactantes:

| Feature            | Diff Relativa | Cohen’s d | Interpretação                          |
| ------------------ | ------------- | --------- | -------------------------------------- |
| horas_planejamento | **132%**      | 0.18      | pedidos atrasados quase dobram o tempo |
| horas_conferencia  | **97%**       | 0.17      | gargalo importante                     |
| horas_coleta       | **77%**       | 0.17      | dificuldade de coleta aumenta o risco  |
| m3                 | **65%**       | 0.10      | pedidos volumosos atrasam mais         |
| peso               | **56%**       | 0.08      | peso interfere no manuseio             |
| horas_divisao_ocam | **41%**       | 0.23      | divisão de OCAMs é forte indício       |

---

## ✔ Interpretação Técnica

* **Diff_rel% alto** → há clara diferença de comportamento entre atrasos e não atrasos.
* **Cohen’s d baixo (< 0.5)** → efeito pequeno, porém **estatisticamente consistente devido ao grande volume amostral**.
* Modelos não lineares tendem a capturar esses efeitos com muito mais precisão.

---

# **5. Visualizações Inferenciais**

Foram gerados boxplots lado a lado para **todas as variáveis numéricas**, mostrando:

* distribuição em atrasos vs não atrasos,
* medianas deslocadas,
* caudas mais pesadas no grupo de atraso,
* concentração de outliers operacionais.

Além disso, foram criadas features derivadas:

* `lead_time_total_horas`
* `complexidade_operacional`
* `pedido_grande_flag`
* `processo_longo_flag`

Comportamentos observados:

* **Pedido grande** → quase sempre associado ao atraso.
* **Processo longo** → ocorre em ambos os grupos → indica **ineficiência sistêmica geral**.

---

# **Conclusões Gerais da Estatística Inferencial**

1. **Peso, volume, m³ e complexidade operacional** aparecem como fortes potenciais explicadores do atraso.
2. ANOVA confirma que **quase todas as etapas são significativamente diferentes** entre pedidos atrasados e não atrasados.
3. Qui-Quadrado mostra que **categorias (cliente, veículo, UF, modalidade)** influenciam fortemente o atraso.
4. Diferenças relativas mostram que pedidos atrasados possuem **lead times praticamente dobrados** em etapas críticas.
5. Mesmo com correlações baixas, o comportamento conjunto das features indica **padrões não-lineares**, perfeitos para modelos como Random Forest, XGBoost e Gradient Boosting.
6. As variáveis derivadas reforçam padrões estruturais:

   * **Pedido grande = risco alto**,
   * **Lead time longo = gargalo transversal**,
   * **Complexidade operacional = determinante de performance**.

---

<div align="left">
  <a href="#topo" title="Voltar ao início do README">⬆️ Topo</a>
</div>

---