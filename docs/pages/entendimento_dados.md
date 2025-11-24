# 🗂 Entendimento dos Dados  
*(CRISP-DM — Etapa 2)*

<a href="../../README.md" title="Voltar para a página principal">
🏠 Voltar para Home
</a>

## 📦 Fonte do Dataset

Dataset Banco de Dados SQL Server
**Tabelas:**  DB_ZT_GERAL_PEDIDOS e DB_ZT_GERAL_ACOMPANHAMENTO_OPERACIONAL

---

## 📊 Estrutura Geral

| Informação | Valor |
|-----------|-------|
| Total de transações | 487.391 |
| Fora do Prazo | 130.499 |
| Tipo do problema | Classificação binária |
| Tipo de dados | Tabelar |

---

## 🧬 Dicionário de Variáveis

Tipos de Dados
| Tipo | Volume | Features  |
|------|--------|-----------|
object |	64	  |[sigla_cliente, nome_cliente, dt_solicitacao, os, tipo_veiculo, destinatario, id_regiao, uf, cidade, cep,   epresentante, flag_entrega_agendada, data_real_prevista_entrega, prazo_inicial_entrega_cliente, data_entrega, fase, desc_fase, prazo_zt, prazo_cliente, dt_fim_emissao, exped_minuta, hora_minuta, transportador, transp_parceiro, modalidade, campanha_pedido, recebedor, status_pedido, penultima_ocorrencia, ultima_ocorrencia, motivo_atraso, departamento, data_agendamento, dt_carga, sigla_cliente.1, dt_nf, os.1, lacre, solicitante, uf.1, status, dt_solicitacao.1, dt_pre_conferencia, dt_distribuicao_cotas, dt_planeja, data_prazo_zenatur, dt_ocam, dt_inicio_coleta, dt_fim_coleta, dt_inicio_conferencia, dt_fim_conferencia, dt_fim_emissao.1, analise_producao, dt_minuta, dt_criacao_minuta, dt_exped_minuta, analise_expedicao, dt_prazo_limite_cliente, dt_emissao_nf, modalidade.1, alocado_em, finalizado_em, data_entrega.1, analise_transporte] |
| float64 |	28 | [placa, peso, m3, minuta, nf_zt, nf_cli, peso.1, horas_pre_conferencia, dias_pre_conferencia, horas_planejamento, dias_planejamento, horas_divisao_ocam, dias_divisao_ocam, horas_coleta, dias_coleta, horas_conferencia, dias_conferencia, horas_emissao, dias_emissao, horas_analise_producao, dias_analise_producao, horas_minuta, dias_minuta, horas_exped_minuta, dias_minuta_exped_minuta, minuta.1, hora_analise_transporte, dias_analise_transporte] |
| int64 | 21 | [ss, nf, nf_cliente, rota, qtde_itens, volume, fl_base, ordem_fase, fl_atraso_zt, fl_atraso_cli, fl_em_atraso, fl_sem_minuta, fl_coleta_cancelada, fl_canhoto, ss.1, qtde_ocams, qtde_itens.1, volume.1, peso_cubado_rodoviario, horas_distribuicao_cotas, dias_distribuicao_cotas] |

---

## 🧭 Qualidade inicial dos dados

| Aspecto | Situação |
|---------|----------|
| Missing values | presente |
| Outliers | Presente |
| Balanceamento | Extremamente desbalanceado |
| Formato | Banco de Dados |
| Dtypes | Todos |

---

## 🧪 Hipóteses iniciais

- Os prozos de entrega pode ser afetado pelo volume de itens
- Quantidade de itens, volumes, OCAM geram complexidade na operação  

---

## 🔧 Primeiras ações tomadas nesta etapa

1. Verificação de missing  
2. Estatística descritiva  
3. Histograma e boxplots  
4. Estatistica inferencial
5. Avaliação de skewness/kurtosis  
6. Preparação para EDA descritiva e inferencial  

---

## 🧪 Conclusão

Esta etapa confirmou que:  
- O dataset necessita de tratamento 
- Extremamente desbalanceado  
- Possibilidade de aprendizado supervisionado  
- Necessita tratamento avançado para recall  
- Possui variáveis categóricas  

**A partir daqui, entramos no EDA.**
<details>
<summary>Clique para Expandir</summary>

- [EDA Estatística Descritiva](./eda_descritiva.md)
- [EDA Estatística Inferencial](./eda_inferencial.md)

</details>

---

<div align="left">
  <a href="#topo" title="Voltar ao início do README">⬆️ Topo</a>
  <a href="../README.md" title="Retornar ao menu principal"> ⬅️ Voltar para Home </a>
</div>

---