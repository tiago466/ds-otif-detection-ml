# EDA - Tratamento dos Dados e Estatistica Descritiva

<a href="../../README.md" title="Voltar para a página principal">
🏠 Voltar para Home
</a>

## Visão Geral

Este notebook é dedicado à etapa de **Preparação dos Dados** dentro do processo CRISP-DM.
Aqui são aplicadas todas as técnicas de limpeza, padronização e estruturação necessárias para garantir que o dataset esteja íntegro, consistente e pronto para as etapas seguintes de análise estatística e modelagem preditiva.

Esta fase é crítica, uma vez que a qualidade dos dados influencia diretamente a performance dos modelos e a confiabilidade das conclusões analíticas.

As operações contempladas incluem:

- remoção de colunas irrelevantes ou redundantes
- correção de inconsistências estruturais
- padronização de tipos (quantitativos vs. categóricos)
- tratamento de valores nulos
- correção de valores negativos em variáveis temporais
- reorganização final do dataset tratado

O resultado desta etapa será um arquivo `.csv` limpo e devidamente tratado, que servirá como insumo para o notebook **01_eda_descritiva.ipynb**.

---

## Objetivo

O objetivo deste notebook é preparar o dataset bruto para análises estatísticas mais robustas, garantindo:

1. **Integridade estrutural**

   - Remoção de colunas que não contribuem para o modelo
   - Eliminação de duplicatas e inconsistências

2. **Correção semântica dos dados**

   - Ajuste de valores negativos
   - Conversão de tipos
   - Padronização de valores categóricos

3. **Tratamento de valores ausentes**

   - Imputação com 0 para variáveis quantitativas
   - Imputação com “NÃO DEFINIDO” para variáveis categóricas

4. **Disponibilização de um dataset pronto para uso**, com o nome:

   ```
   acompanhamento_operacional_clean.csv
   ```

   armazenado em:

   ```
   database/processed/
   ```

Este notebook conclui a etapa de **Preparação dos Dados** e libera o conjunto para a próxima fase:
**Análise Estatística Descritiva (Notebook 01)**

---

# Importações

# 1. Carregamento e Visualização Preliminar

***Descrição:*** Utilizando o dataset de acompanhamento operacional dos pedidos.

## Baixando a Fonte de Dados

# 2. Estrutura dos Dados

***Descrição:*** Diagnostico geral dos dados, como formatos e integridade dos dados
> - Linhas e colunas  
> - Tipo das variáveis  
> - dados nulos  
> - dados duplicados  
> - dados impossíveis  

> **Nota Técnica:** Durante a etapa de modelagem será necessário avaliar rigorosamente a relevância das variáveis de data brutas como `dt_solicitacao`, `dt_pre_conferencia`, `dt_distribuicao_cotas`, `dt_ocam`, entre outras em comparação com as variáveis derivadas que já representam o tempo transcorrido em cada etapa (`dias_pre_conferencia`, `dias_planejamento`, `dias_divisao_ocam`, etc.).
>
> Isso porque, em muitos cenários de modelagem supervisionada, **as durações entre eventos** (features derivadas) tendem a ser mais informativas para prever atraso do que **as datas absolutas**, que podem introduzir ruído ou complexidade desnecessária. Entretanto, a utilidade de cada grupo será validada empiricamente por meio de testes estatísticos e importância de features.
>
> Independentemente da decisão final sobre quais atributos serão utilizados na modelagem, **todas as colunas de data serão devidamente tratadas**, convertidas para o tipo `datetime` e organizadas de forma consistente para permitir:
>
> * validações cronológicas,
> * extração de novas features temporais (ex.: dia da semana, lead times, time deltas),
> * criação de indicadores de sequência operacional,
> * e auditoria da ordem dos eventos no processo.
>
> As variáveis de data atualmente identificadas incluem (lista consolidada, sujeita a ajustes conforme novas análises):
>
> * `dt_solicitacao`, `dt_pre_conferencia`, `dt_distribuicao_cotas`, `dt_planeja`, `data_prazo_zenatur`,
> * `dt_ocam`, `dt_inicio_coleta`, `dt_fim_coleta`,
> * `dt_inicio_conferencia`, `dt_fim_conferencia`,
> * `dt_fim_emissao`, `analise_producao`,
> * `dt_minuta`, `dt_criacao_minuta`, `dt_exped_minuta`, `analise_expedicao`,
> * `dt_prazo_limite_cliente`, `dt_emissao_nf`,
> * `data_entrega`, `data_real_prevista_entrega`,
> * `prazo_inicial_entrega_cliente`, `prazo_zt`, `prazo_cliente`,
> * `data_agendamento`.
>
> Para fins de organização e clareza metodológica, as variáveis serão **separadas em dois grupos principais**:
>
> **(a) Colunas de datas:** todas as variáveis temporais em formato datetime, utilizadas para análises sequenciais, geração de deltas e validação da coerência operacional.
>
> **(b) Colunas categóricas:** variáveis não numéricas que representam estados, classificações ou atributos qualitativos do pedido ou da operação.
>
> Essa separação facilita o fluxo do pré-processamento, evita erros de tipagem, e permite aplicar métodos estatísticos e algoritmos adequados a cada classe de variável, preservando a integridade e a robustez do modelo final.

> **Nota Técnica:** A presença de valores nulos em diversas variáveis requer atenção especial durante o tratamento dos dados, pois, no contexto logístico, a ausência de informação não representa necessariamente um erro ou falha de coleta. Em muitos casos, os nulos refletem o comportamento real do processo operacional e podem influenciar diretamente o TARGET de atraso utilizado no modelo preditivo de OTIF.
>
> Um exemplo relevante é o conjunto de variáveis relacionadas ao processo de **OCAM** (Organização, Conferência e Arrumação de Materiais), como `dt_ocam` e `dias_divisao_ocam`.
> Quando essas variáveis aparecem como nulas, isso indica que **o pedido não passou pela etapa de divisão de OCAM**, o que por si só é uma informação operacional importante e pode impactar o desempenho da entrega.
>
> **Contexto da Regra de Negócio – OCAM:**
> A etapa de OCAM ocorre quando uma mesma SKU está distribuída em locais distintos dentro da operação da Zenatur, seja entre setores da matriz ou entre diferentes galpões.
> Esse processo também é acionado quando um pedido possui grande volume ou demanda logística complexa, exigindo a divisão do item em múltiplas unidades operacionais.
>
> A divisão de OCAM, portanto, pode introduzir atrasos significativos, principalmente quando:
>
> * os materiais estão dispersos em galpões distintos;
> * há necessidade de consolidação física dos itens antes da expedição;
> * ou quando o processo de separação é mais demorado devido ao volume.
>
> Dessa forma, **os valores nulos relacionados ao OCAM não podem ser simplesmente imputados ou descartados**, pois carregam significado semântico dentro do processo logístico.
> Eles devem ser tratados como potenciais **indicadores de ausência da etapa**, podendo inclusive serem convertidos em variáveis binárias (“passou por OCAM / não passou por OCAM”) para enriquecer o modelo.
>
> Em resumo, o tratamento dos nulos nesse caso deve ser orientado pelo entendimento operacional, garantindo que a transformação preserve o significado real da cadeia logística e evite comprometer a previsão final do OTIF.

> **Nota Técnica:** Não foi detectado linhas duplicadas.

> **Nota Técnica:** As features quantitativas devem ser positivas.
> - Inicialmente remover as colunas de **dias** emantar **horas**

> **Nota Técnica:** Para fins de análise exploratória e preparação dos dados, realizamos a classificação das variáveis do dataset em duas categorias principais: **Variáveis Categóricas (Qualitativas)** e **Variáveis Quantitativas (Numéricas)**. Essa distinção é essencial para o correto tratamento estatístico, para a definição de técnicas adequadas de pré-processamento e para o desenvolvimento de modelos preditivos consistentes.
>
> ### **1. Variáveis Categóricas (Qualitativas)**
>
> Compreendem atributos que representam *classes*, *etapas*, *nomes*, *status* ou *categorias operacionais*. São variáveis que não expressam magnitude numérica, mas sim características qualitativas do processo logístico.
>
> Durante a avaliação estrutural, **não foram identificados valores inválidos ou anomalias lógicas** nesse grupo de variáveis. A integridade categórica se mostrou adequada, embora etapas posteriores poderão demandar:
>
> - padronização de capitalização,
> - redução de categorias raras,
> - agrupamento semântico,
> - e codificação adequada para modelos supervisionados (ex.: One-Hot Encoding ou Target Encoding).
>
> ### **2. Variáveis Quantitativas (Numéricas)**
>
> Incluem atributos inteiros e de ponto flutuante que representam quantidades, medidas operacionais e tempos de processo como pesos, volumes, horas e dias entre etapas.
>
> De acordo com as regras de negócio aplicáveis à operação logística da Zenatur, **nenhuma dessas variáveis deve assumir valores negativos**, uma vez que tempos, pesos e quantidades são, por natureza, não negativos.
>
> A inspeção revelou **oito variáveis numéricas contendo valores negativos**, destacando-se a coluna `horas_conferência`, que apresentou **5.558 ocorrências** desse tipo.
>
> A presença desses valores exige investigação adicional, pois podem indicar:
>
> - inconsistências geradas durante a extração,
> - erros de cálculo na geração de variáveis derivadas,
> - falhas de registro operacional,
> - ou situações em que a ordem temporal dos eventos foi registrada incorretamente.
>
> Essas variáveis deverão ser tratadas de forma criteriosa antes da modelagem, garantindo que sua representação reflita corretamente o fluxo operacional e não introduza distorções nos algoritmos preditivos.

## Conclusão Geral

**Descrição:**
A análise estrutural do dataset permitiu identificar um conjunto consistente de variáveis relevantes para o estudo preditivo de OTIF, bem como diversos aspectos que exigem tratamento criterioso antes do início da Estatística Descritiva e da etapa de modelagem.
A seguir, são destacados os principais pontos observados e as recomendações para o pré-processamento.

### **1. Colunas candidatas à remoção**

Com base na avaliação de redundância, coerência semântica, utilidade preditiva e qualidade dos dados, foram identificados três grupos de variáveis potencialmente elegíveis para remoção: **categóricas**, **temporais** e **quantitativas derivadas**.

#### **1.1 Variáveis Categóricas**

Foram identificadas diversas colunas categóricas redundantes, duplicadas, pouco informativas ou sem relação direta com o fenômeno de atraso operacional. A remoção dessas variáveis contribui para:

- reduzir ruído no modelo,
- evitar multicolinearidade categórica,
- facilitar a engenharia de atributos,
- diminuir dimensionalidade desnecessária.

Entre as variáveis categóricas candidatas à remoção incluem-se:

```
'os.1', 'modalidade.1', 'sigla_cliente.1', 'uf.1', 'dt_solicitacao.1', 'dt_fim_emissao.1', 'data_entrega.1', 'nome_cliente', 'os', 'id_regiao', 'cidade', 'cep', 'desc_fase', 'transportador', 'transp_parceiro', 'campanha_pedido', 'recebedor', 'status_pedido', 'penultima_ocorrencia', 'ultima_ocorrencia', 'solicitante', 'lacre', 'destinatario', 'departamento'
```

A remoção será executada após verificação final de impacto na modelagem.

#### **1.2 Variáveis de Data**

As datas originais foram incluídas no dataset com a finalidade de permitir o cálculo das diferenças temporais entre as etapas operacionais (dias/horas de cada fase). Uma vez que essas variáveis derivadas já estão presentes e capturam a essência temporal necessária para o modelo, as datas brutas tornam-se, em grande parte, redundantes.

Além disso:

- **o processo de solicitação de pedidos não apresenta sazonalidade forte** ao longo do ano,
- eventuais efeitos sazonais (ex.: férias escolares, picos de fim de ano, feriados prolongados) podem existir, mas tendem a ter **baixo impacto direto** na previsão de atraso operacional,
- ainda assim, caso haja necessidade, tais efeitos podem ser avaliados futuramente via testes de hipótese ou decomposição temporal.

Por esses motivos, as colunas de datas são fortes candidatas à remoção, mantendo-se apenas aquelas essenciais para o cálculo de deltas ou verificações cronológicas.

#### **1.3 Variáveis Quantitativas Derivadas (Horas)**

O dataset contém diversas variáveis contínuas expressas em “dias” como: `dias_pre_conferencia`, `dias_coleta`,`dias_distribuicao_cotas` etc.
Essas variáveis apresentam três desafios:

1. **Alta volatilidade Intrahora** e baixa interpretabilidade operacional devido a media de entregas serem no mesmo dia;
2. **Alternância brusca** de escala entre pedidos, dificultando normalização;
3. Existência de valores negativos e inconsistentes, que exigem correção ou exclusão.

Além disso, o dataset já contém uma versão **agregada e mais estável** dessas variáveis: as colunas em horas (`horas_pre_conferencia`, `horas_planejamento`, etc.), que são mais adequadas para modelagem preditiva.

Com isso, as seguintes variáveis são candidatas à remoção:

```
'dias_pre_conferencia', 'dias_planejamento', 'dias_divisao_ocam', 'dias_coleta', 'dias_conferencia', 'dias_emissao', 'dias_analise_producao', 'dias_minuta', 'dias_minuta_exped_minuta', 'dias_analise_transporte', 'dias_distribuicao_cotas'
```

O uso exclusivo das versões em *dias* simplifica o modelo e reduz ruído.

---

### **2. Síntese Estratégica**

Com base na análise estrutural, conclui-se que:

- O dataset é **adequado para análise estatística e modelagem**, desde que passe por transformações essenciais.
- A remoção de colunas redundantes ou ruidosas **aumentará a qualidade do modelo**, reduzindo dimensionalidade e evitando inconsistências.
- O tratamento de nulos deve ser **orientado por regras de negócio**, especialmente no caso de etapas como OCAM, conferência, expedição e emissão.
- Variáveis temporais devem ser convertidas, auditadas e avaliadas para manter apenas aquelas com valor preditivo real.
- O conjunto de variáveis derivadas em dias fornece uma base mais estável e representativa do ciclo operacional.
- Após o pré-processamento adequado, o dataset estará plenamente preparado para avançar para a fase de Estatística Descritiva, Feature Engineering e, posteriormente, para a modelagem supervisionada do atraso (OTIF).

---

# 3. Tratamento dos Dados

***Descrição:***
Esta etapa tem como objetivo realizar a limpeza, padronização e preparação inicial do dataset, assegurando que as informações estejam adequadas para a aplicação das técnicas de Estatística Descritiva e para as fases subsequentes de modelagem preditiva.
O tratamento adequado dos dados é essencial para reduzir ruído, corrigir inconsistências e fortalecer a qualidade analítica do modelo final.

## Procedimentos incluídos nesta etapa:

> **Remoção de colunas irrelevantes ou redundantes**
> Elimina-se do dataset principal as variáveis categóricas, temporais ou quantitativas que não agregam valor analítico, sejam duplicadas, inconsistentes, sem relevância para a modelagem ou já representadas por atributos derivados mais informativos.
>
> **Tratamento dos valores nulos**
> Conforme a natureza da variável:
> – Variáveis quantitativas terão valores nulos substituídos por `0`, representando ausência da etapa ou inexistência do evento.
> – Variáveis categóricas receberão o marcador `"NÃO DEFINIDO"`, preservando o significado semântico sem introduzir distorções estatísticas.
> Esse procedimento garante completude para análises descritivas e facilita a vetorização nas próximas fases.
>
> **Tratamento dos valores negativos**
> Valores negativos são invalidados em variáveis que, por regra de negócio, devem ser não negativas (como tempos, quantidades e medidas operacionais).
> Esses registros serão corrigidos, substituídos ou analisados pontualmente, garantindo consistência lógica do dataset e evitando impactos indevidos nas estatísticas e na modelagem.

## Remoção das Colunas

# Criando um novo dataset

# Conclusão Geral – Tratamento dos Dados

Após a etapa de higienização e organização dos dados, o dataset `df_main` encontra-se devidamente preparado para avançar para as análises de Estatística Descritiva. As transformações aplicadas garantiram consistência interna, eliminação de ruído, padronização semântica e conformidade com as regras operacionais da cadeia logística da Zenatur.

A seguir, apresentam-se os principais resultados e conclusões do processo de tratamento:

---

## **1. Remoção de Colunas Irrelevantes ou Redundantes**

Foram excluídas variáveis categóricas, temporais e quantitativas que apresentavam:

* redundância estrutural (ex.: colunas duplicadas),
* baixa relevância preditiva,
* inconsistências semânticas,
* ou ausência de utilidade operacional dentro do escopo do modelo de OTIF.

A remoção dessas colunas aprimorou a clareza do dataset e reduziu sua dimensionalidade, mantendo apenas atributos com potencial informativo real para a análise exploratória e futura modelagem preditiva.

---

## **2. Estrutura Final do Dataset**

Após o tratamento, o dataset consolidado (`df_main`) passou a conter:

### **• 12 variáveis quantitativas contínuas (float64):**

Principalmente métricas de tempo operacional expressas em dias, além de medidas de peso e volume.

### **• 10 variáveis categóricas (object):**

Atributos qualitativos que representam características logísticas, status operacional, modalidades, representações e indicadores relevantes para o fluxo de pedido.

### **• 10 variáveis quantitativas inteiras (int64):**

Contagens, flags binárias e medidas discretas associadas à operação, como quantidade de itens, indicadores de atraso, base logística e número de OCAMs.

Essa composição garante um balanço saudável entre variáveis descritivas e operacionais, preservando o significado logístico do processo.

---

## **3. Tratamento de Valores Nulos**

A imputação foi realizada de acordo com as regras de negócio:

* **Variáveis quantitativas:** substituição por 0, representando ausência de tempo, quantidade ou duração na etapa correspondente.
* **Variáveis categóricas:** substituição por `"NÃO DEFINIDO"`, distinguindo casos sem registro operacional de categorias efetivas.

Esse procedimento minimiza perdas de informação e mantém a integridade da interpretação operacional, especialmente em etapas opcionais ou não ocorridas do processo logístico.

---

## **4. Correção de Valores Negativos**

Valores negativos foram identificados exclusivamente em colunas quantitativas derivadas, referentes a tempos operacionais. Por serem inconsistentes com o fluxo logístico — onde durações não podem assumir valores negativos — todas as ocorrências foram corrigidas utilizando **valor absoluto (`abs()`)**, solução segura e vetorizada, mantendo a magnitude temporal correta sem comprometer o significado das variáveis.

---

## **5. Resultado Final**

O dataset `df_main` encontra-se agora:

* **limpo**,
* **consistente**,
* **estruturalmente sólido**,
* **sem valores nulos**,
* **sem valores negativos**,
* **sem colunas redundantes**,
* **com tipagem adequada**,
* **e pronto para a próxima etapa do CRISP-DM**:
  ✔ **Estatística Descritiva**.

Essas transformações garantem que a análise exploratória, a engenharia de atributos e, posteriormente, a modelagem preditiva para estimativa de atraso (OTIF) ocorram sobre uma base robusta, coerente e aderente ao contexto operacional da Zenatur.

---

<div align="left">
  <a href="#topo" title="Voltar ao início do README">⬆️ Topo</a>
</div>

---

# EDA - Estatistica Descritiva

<a href="../../README.md" title="Voltar para a página principal">
🏠 Voltar para Home
</a>

## Visão Geral

A Estatística Descritiva compreende o conjunto de técnicas voltadas à exploração inicial de um conjunto de dados, com foco na compreensão da distribuição, comportamento, padrões centrais, variabilidade e possíveis anomalias.  
Nesta etapa, o objetivo principal é obter uma leitura clara da estrutura do dataset, identificar problemas de integridade e avaliar características fundamentais que influenciarão diretamente na modelagem preditiva.

As análises contemplam os seguintes pilares:
- identificação de medidas centrais (média, mediana, moda)
- avaliação de dispersão (variância, desvio padrão e coeficiente de variação)
- estudo da forma da distribuição (assimetria e curtose)
- investigação de outliers estatísticos e lógicos
- análise da frequência de variáveis categóricas
- avaliação de correlações entre variáveis numéricas
- análise da integridade e consistência estrutural do dataset

Estas informações formam o alicerce para as próximas etapas do CRISP-DM, especialmente Preparação dos Dados e Modelagem.

## Objetivo

O objetivo desta etapa é aplicar técnicas de **Análise Estatística Descritiva** utilizando Python e as bibliotecas **NumPy** e **Pandas**, com apoio de tabelas e visualizações gráficas.
A análise descritiva tem como finalidade compreender a estrutura, qualidade e comportamento das variáveis do dataset, servindo como base para decisões de pré-processamento, feature engineering e modelagem preditiva.

A partir desta etapa, buscamos responder às seguintes questões fundamentais sobre o conjunto de dados:

1. **Existem valores ausentes (missing values)?**
   Quantos são? Em quais colunas se concentram? Representam ausência legítima ou falha de coleta?

2. **Existem registros duplicados?**
   Devem ser removidos? Qual a regra de unicidade aplicável ao dataset?

3. **Cada variável está corretamente tipada?**
   Datas estão reconhecidas como `datetime`?
   Variáveis numéricas foram importadas como texto?
   Campos categóricos estão mapeados como `object`?

4. **Existem valores inválidos ou logicamente impossíveis?**
   Exemplos: valores negativos em atributos que não deveriam assumir tais valores, datas inconsistentes ou fora de ordem, quantidades incompatíveis com o processo operacional.

5. **Qual é a tendência central das variáveis numéricas?**
   Avaliação de média, mediana e moda, identificando o comportamento central e possíveis distorções.

6. **Qual é o grau de dispersão dos dados?**
   Análise de variância, desvio padrão e coeficiente de variação para verificar estabilidade ou heterogeneidade das medidas.

7. **As variáveis apresentam simetria ou assimetria?**
   Cálculo de *skewness* e *kurtosis* para identificar distribuições alongadas, achatadas ou com caudas extremas.

8. **Como se comportam as distribuições de cada variável?**
   Por meio de histogramas, densidades, boxplots e outras representações visuais.

9. **Existem outliers extremos ou anomalias estatísticas?**
   Identificação via IQR, Z-score ou inspeção gráfica, avaliando o impacto no processo e na futura modelagem.

# Importações

# 1. Carregamento e Visualização Preliminar

***Descrição:*** Utilizando o dataset de acompanhamento operacional dos pedidos tratados.
> **Arquivo e:** database/processed/acompanhamento_operacional_clean.csv

# 2. Tendencias Centrais - Medidas de Centralidade (Média, Mediana, Moda)

***Descrição:*** Entender a natureza e a distribuição das variáveis.  
As tendências centrais, ou medidas de centralidade, são valores únicos que representam o centro de um conjunto de dados, sendo a média, a mediana e a moda as mais comuns. Elas servem para resumir dados de forma mais simples, como a idade de um grupo de 100 pessoas, salario de um grupo de funcionarios, etc. A escolha de qual medida usar depende da natureza dos dados, como a presença de valores extremos que podem influenciar a média. 

**Medidas e Visualizações**
- Média
- mediana
- moda

> - **Se mean e 50% (mediana)** estão próximos → boa simetria.
> - **Se min e max** estão muito distantes → alto desvio padrão (talvez outliers).
> - **Se std é da mesma ordem** de grandeza da média → alta variabilidade.

## Visão Geral das Medidas de Centralidade

- Avaliar e classificar as medidas de centralidade das 17 features quantitativas
- Avaliar e classificar o tamanho da cauda e classificar cada featere como: Simétrica, assimétrica esquerda, assimétria a direita
- Avaliar o desvio padrão vs medias, verificar as proximidades de cada feature
- Verificar skewness e kurtosis de cada feature

> 💡 **Nota Técnica:** 
> As estimativas das medidas de centralidade foram aplicadas na base de dados consolidada, ou seja, com a granularidade mais alta, para observar o comportamento geral dos dados.

**Nota Ténica:** A análise estrutural das variáveis quantitativas evidencia um padrão estatístico marcante: **todas apresentam forte assimetria à direita**, caracterizada pela presença de **caudas longas** que se estendem para valores muito superiores ao comportamento central da distribuição.

Esse diagnóstico emerge prontamente quando comparamos as medidas de centralidade, especialmente **média** e **mediana**. Observou-se que, para praticamente todas as features operacionais, a **mediana** encontra-se concentrada entre **0 e 10 horas**, enquanto as **médias** assumem valores muito mais elevados. Essa disparidade sistemática, **média muito maior que a mediana** sugere a existência de **observações extremas** que distorcem a média aritmética, fenômeno típico de distribuições com **outliers estruturais**.

Em outras palavras, o comportamento observado indica que:

- a maioria dos pedidos é processada de forma rápida (medianas baixas);
- porém, um pequeno conjunto de pedidos apresenta tempos **profundamente discrepantes**, produzindo **caudas longas** e elevando consideravelmente as médias;
- essa discrepância é consistente com a dinâmica real de processos logísticos, nos quais atrasos pontuais — embora raros — têm grande impacto no desempenho operacional e, consequentemente, nos indicadores de OTIF.

Assim, a assimetria à direita encontrada não é apenas estatisticamente esperada, mas também operacionalmente significativa, reforçando o entendimento de que **os atrasos logísticos são eventos esparsos, porém severos**, e constituem justamente o fenômeno que o modelo preditivo deverá capturar.

> ***Observações:*** foi destacado o tempo de processo apenas para facilitar a esposição, mas observa-se que existem a disparidade em todos as variaveis: no `peso` notodamos que até 75% dos dados pesam até 17.73 kg, ou seja 2/3 dos dados, contudo os 25% restantes se tramtam dos valores da ponta da cauda longa, que distorcem as médias com o valor máximo de 90.390 Kg.

# 3. Medidas de Dispersão (Variância, Desvio-Padrão e Coeficiente de Variação)

***Descrição:***
As medidas de dispersão avaliadas nesta etapa têm como objetivo quantificar **o grau de variabilidade** das variáveis numéricas. Enquanto as medidas de tendência central mostram *onde* os dados tendem a se concentrar, as medidas de dispersão mostram *o quanto* os dados se afastam desse centro.

Essas medidas são fundamentais para compreender:

- a estabilidade do processo operacional,
- a existência de variabilidade excessiva (ruído ou eventos críticos),
- o impacto de valores extremos nas médias,
- e o grau de risco estatístico associado a cada etapa do fluxo logístico.

As análises desta etapa complementam diretamente o estudo de assimetria e preparam o terreno para as próximas fases de correlação e inferência.

---

## **Medidas e Visualizações**

- **Variância (`var`)** — indica o quanto os valores se dispersam em relação à média.
- **Desvio-Padrão (`std`)** — raiz da variância; mostra a dispersão na mesma escala da variável.
- **Coeficiente de Variação (`CV = std / mean`)** — mede a variabilidade relativa, permitindo comparação entre variáveis de escalas diferentes.

---

### **Interpretações Importantes**

> - **Se std é alto** → grande instabilidade operacional; pode indicar gargalos, atrasos pontuais ou processos imprevisíveis.
> - **Alta Dispersão - Se CV > 0.3** (30%) → dispersão maior que a média → forte volatilidade; comportamento caótico.
> - **Dispersão Moderada - Se CV entre 0.15 e 0.3** (15% - 30%) → variabilidade moderada; processos alternam entre normal e crítico.
> - **Baixa Dispersão - Se CV < 0.15** → variabilidade baixa; processo estável.

---

### **Sinalizações práticas para OTIF**

- Variáveis com **alto std** ou **alto CV** tendem a ser **ofensores operacionais**, contribuindo para atrasos.
- Variáveis com **baixo desvio** indicam processos mais previsíveis e estáveis.
- Comparar CV entre colunas poderá evidenciar quais etapas “puxam a cauda” da distribuição.

**Nota Ténica:** As variáveis quantitativas do dataset apresentam **altíssima dispersão**, indicando grande heterogeneidade no comportamento operacional dos pedidos.
A combinação de **desvio-padrão elevado**, **variâncias muito altas** e **coeficientes de variação (CV) acima de 100%** em todas as features confirma que o processo logístico analisado possui **long tail** — ou seja, a maior parte dos pedidos é simples, mas existe um conjunto menor de pedidos altamente complexos que gera grande instabilidade nos tempos operacionais.

### Principais Evidências

- O **CV** (desvio-padrão / média) alcança valores extremos como **2239%** (volume), **1120%** (horas de emissão) e **1099%** (peso cubado), revelando que a variabilidade relativa é **muitas vezes maior que a própria média**.
- A **mediana muito baixa** (muitas vezes igual a zero) contrasta com médias elevadas, mostrando que poucos casos extremos são responsáveis pela maior parte do tempo operacional.
- O **erro padrão baixo** indica que a média é estatisticamente estável devido ao grande volume amostral, mas isso não reduz a dispersão — apenas mostra que a média é representativa *do caos*.
- A presença de valores máximos em ordens de grandeza muito superiores ao Q3 confirma a existência de **outliers operacionais legítimos**, ligados a pedidos complexos (muitas linhas, grandes volumes, OCAM alto, rotas longas, análise demorada, conferências específicas etc.).

### Interpretação Operacional

Essa dispersão não é ruído, ela reflete exatamente os cenários que **quebram o OTIF**. Pedidos simples têm tempos baixos; pedidos complexos acumulam horas em várias fases, puxando as médias para cima e ampliando drasticamente a variância.

### Conclusão Técnica

As medidas de dispersão demonstram que:

- O processo logístico da Zenatur é **altamente variável**;
- Existem **padrões operacionais críticos** concentrados em um subconjunto de pedidos;
- Essa variabilidade extrema precisa ser considerada na modelagem preditiva, pois é justamente o padrão que diferencia entregas **no prazo** de entregas **fora do prazo**.

Essa análise encerra a etapa de **Medidas de Dispersão** e prepara o terreno para o próximo passo do EDA: **Medidas de Forma (Skewness & Kurtosis)** e posteriormente a **Estatística Inferencial**, onde investigaremos *por que* esses cenários ocorrem.

# 5. Forma da Distribuição — Assimetria (Skewness) e Curtose (Kurtosis)

## ***Descrição:***

As medidas de forma da distribuição complementam a análise descritiva, avaliando **como os valores de uma variável se distribuem em torno da média**.
Enquanto a tendência central e a dispersão mostram o “tamanho” e o “espalhamento”, a Forma da Distribuição revela **comportamentos extremos, caudas longas e picos atípicos** fundamentais para entender processos logísticos com OTIF.

## **Assimetria (Skewness)**

A Assimetria mede o grau e a direção da inclinação da distribuição:

| Tipo         | Skewness | Interpretação                                  |
| ------------ | -------- | ---------------------------------------------- |
| Neutra       | = 0      | distribuição normal simétricaNormal            |
| Positiva     | > 0      | assimetria à direita (cauda longa à direita)   |
| Negativa     | < 0      | assimetria à esquerda (cauda longa à esquerda) |

No contexto operacional:

> **Assimetria positiva (Skew > 0)** indica poucos pedidos com tempos muito altos em alguma etapa, exatamente o padrão que quebra a OTIF, ou tambem divisões de OCAMs expressívas, altas quantidade de linhas (quantidade de itens) produzidos.

---

## 🔹 **Curtose (Kurtosis)**

A Curtose avalia o “formato do pico” da distribuição:

| Tipo         | Curtose | Interpretação                              |
| ------------ | ------- | ------------------------------------------ |
| Mesocúrtica  | ≈ 3     | Normal                                     |
| Leptocúrtica | > 3     | Pico alto e caudas pesadas → mais outliers |
| Platicúrtica | < 3     | Pico baixo → pouca concentração            |

Em logística:

> **Curtose alta significa que o processo possui “picos extremos”: poucos pedidos muito longos convivendo com muitos pedidos curtos.**

Ou seja, a cara do OTIF da Zenatur.


 **Nota Técnica:** A análise de *Skewness* (assimetria) e *Kurtosis* (curtose) revelou que todas as variáveis quantitativas do dataset apresentam:

- **Assimetria forte à direita (Skewness >> 1)**
- **Curtose elevada (Kurtosis >> 3)**

Esse padrão indica que a operação da Zenatur possui uma distribuição **altamente concentrada em pedidos simples** (valores próximos de zero), mas com um conjunto menor de pedidos **extremamente complexos**, que acumulam muitas horas em etapas como conferência, produção, emissão, minuta, transporte e OCAM.

Em termos operacionais, isso significa que **os atrasos OTIF não são causados por uma única fase**, mas sim pela **soma de pequenos atrasos ao longo de várias etapas**, geralmente associados a:

- pedidos volumosos,
- muitos itens,
- múltiplas divisões de OCAM,
- maior carga produtiva,
- necessidade de movimentações internas,
- reprocessamentos,
- emissões demoradas,
- gargalos específicos do transporte.

Essa estrutura gera distribuições com **caudas longas** e **picos elevados**, características de processos com grande variação e presença de eventos críticos.
Esses eventos extremos são legítimos e representam exatamente os casos que quebram o OTIF, portanto, são essenciais para a modelagem preditiva.

Em resumo, a forma da distribuição confirma que a operação possui um comportamento **long tail**, onde poucos pedidos extremamente complexos impactam de maneira desproporcional o desempenho operacional. Esse diagnóstico encerra a fase de análise descritiva e fundamenta a próxima etapa: avaliação inferencial dos fatores que explicam o atraso.

# 6. Representações Gráficas das Distribuições e Outliers

## Descrição:

A representação gráfica é a etapa final da Estatística Descritiva, permitindo visualizar a distribuição real das variáveis e confirmar padrões previamente identificados por medidas numéricas.
Enquanto as estatísticas de centralidade, dispersão e forma fornecem *indicadores*, os gráficos revelam a *estrutura visual* da amostra — especialmente útil em processos logísticos que naturalmente apresentam assimetria, caudas longas e casos extremos.

## Objetivos desta etapa

* Visualizar a densidade e o formato das distribuições numéricas
* Confirmar visualmente a assimetria e a curtose das variáveis
* Identificar graficamente a presença de outliers
* Avaliar padrões operacionais associados a atrasos de entrega (OTIF)
* Preparar a base para a etapa final do EDA: análise de outliers e estatística inferencial

## Gráficos utilizados

- **1. Histograma + KDE:** Mostra a distribuição geral da variável, concentrando:
- **2. Boxplot:** Ferramenta visual para identificar outliers, amplitude interquartil (IQR), dispersão em torno da mediana e comparação direta entre variáveis.
- **3. Histograma com Escala Logarítmica:** Útil para distribuições extremamente assimétricas que permite visualizar melhor os valores intermediários, evita compressão causada por valores extremos e evidencia padrões que o histograma padrão não mostra

**Nota Técnica:** A identificação de outliers tem como objetivo isolar observações que se afastam de maneira extrema do comportamento central da distribuição. No contexto operacional do OTIF, esses casos extremos não representam “erros” do dataset, mas sim **situações reais que carregam alto impacto logístico**, como pedidos volumosos, fragmentados ou que exigem processamento excepcional.

- **1. Outliers via IQR (Boxplot):** A análise do *Interquartile Range (IQR)* evidenciou que praticamente todas as variáveis quantitativas apresentam caudas longas à direita. Os boxplots mostraram uma grande concentração de observações próximas ao quartil inferior (Q1–Q2) e **um volume expressivo de valores que ultrapassam Q3**, formando aglomerações densas de pontos além dos limites do whisker.

- **2. Distribuição (Histogramas):** Mostram alta concentração de valores próximos de zero, seguidos por uma cauda longa à direita. Isso confirma que a maior parte dos pedidos é simples, mas existe um conjunto pequeno de casos altamente volumosos.

>**Interpretação:**
>Esses outliers representam pedidos muito maiores, mais complexos ou com tempos logísticos significativamente superiores à média — características típicas de operações críticas que elevam o risco de atraso.

---

## **2. Outliers via Z-Score (|z| ≥ 3)**

A análise de Z-Score permitiu quantificar a proporção de observações que se desviam mais de três desvios-padrão da média. O ranking a seguir destaca as variáveis mais críticas:

| Variável                   | % Outliers | Interpretação Operacional                                            |
| -------------------------- | ---------- | -------------------------------------------------------------------- |
| **qtde_ocams**             | **2.30%**  | Indica pedidos fragmentados e SKUs distribuídas em múltiplos pontos. |
| **horas_conferencia**      | 2.06%      | Conferência lenta, conferências extensas ou divergências frequentes. |
| **qtde_itens**             | 2.03%      | Pedidos volumosos; maior probabilidade de gargalo operacional.       |
| **horas_divisao_ocam**     | 1.84%      | Complexidade no processo de divisão e alocação de SKU.               |
| **horas_coleta**           | 1.83%      | Picking fragmentado, distâncias maiores ou pedidos fora do padrão.   |
| **horas_analise_producao** | 1.53%      | Filas ou atrasos acumulados na operação produtiva.                   |

# Conclusão estatística

As variáveis com maior índice de outliers são exatamente aquelas relacionadas ao **volume de itens**, **fragmentação de estoque (OCAM)** e **tempos operacionais**, confirmando a presença de eventos extremos no fluxo logístico. Estes volumes expressívos podem estar ligados diretamente a relevancia do cliente como NTL, PEG, SAM, VRA e COL.

---

## Significado operacional dos outliers

Os outliers identificados não devem ser encarados como ruído ou erro de coleta, mas sim como **eventos críticos que ocorrem naturalmente no processo operacional**. Entre as principais causas:

- pedidos grades com muitos itens que ocupam a linha de produção
- volumes e pesos acima do padrão
- necessidade de múltiplos OCAMs
- picking disperso entre galpões
- fila operacional em conferência, produção e expedição

Em todos os casos, trata-se de situações que realmente **aumentam o tempo de processamento e elevam o risco de ruptura do OTIF**.

---

## Insight-chave da análise

A análise combinada de IQR, Z-Score, skewness, curtose e medidas centrais indica que:

> **Os maiores ofensores estatísticos são exatamente os maiores ofensores operacionais.**
> **Pedidos grandes, complexos e fragmentados respondem pela maior parte dos desvios que prejudicam o OTIF.**

Essa conclusão reforça a importância de tratar os outliers não como exceções a serem removidas, mas como **elementos fundamentais para o aprendizado do modelo preditivo**.

---

## Encerramento da Etapa

Esta análise conclui a fase de detecção e interpretação de outliers na Estatística Descritiva.
Os padrões identificados serão essenciais nas próximas etapas:

- estatística inferencial (diagnóstico das causas)
- análise de correlação
- modelagem preditiva do risco de atraso (OTIF)

