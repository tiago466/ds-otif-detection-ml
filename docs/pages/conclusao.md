# **Conclusão — DS OTIF Detection**

<a href="../README.md" title="Voltar para a página principal">
🏠 Voltar para Home
</a>  

---

O desenvolvimento deste projeto demonstrou, de forma clara e fundamentada, que a previsão de riscos de violação do OTIF na Zenatur é não apenas possível, como altamente eficaz quando estruturada a partir de um pipeline sólido de Ciência de Dados.

O trabalho iniciou com uma investigação profunda das características logísticas, onde foi identificada a complexidade do fluxo operacional e os pontos críticos capazes de influenciar diretamente o cumprimento dos prazos. A etapa de EDA revelou comportamentos importantes como forte assimetria nas distribuições, presença de valores extremos, lacunas temporais e concentrações expressivas em determinadas fases operacionais. Esses elementos explicam a variabilidade dos tempos logísticos e fundamentaram a importância de derivar novas variáveis mais representativas.

Com base nessas inferências, foram criadas features estratégicas, como *lead_time_total_horas*, *complexidade_operacional*, *pedido_grande_flag* e *processo_longo_flag*. Essas variáveis sintetizam aspectos logísticos que aumentam substancialmente o risco de atraso e elevaram significativamente o poder preditivo dos modelos testados.

O pipeline de pré-processamento foi cuidadosamente construído para preservar a integridade dos dados e evitar *data leakage*. Todas as transformações — imputação, codificação categórica e padronização — foram encapsuladas em objetos próprios e ajustadas exclusivamente no conjunto de treino. Além disso, a separação *train/test* respeitou a distribuição de classes, garantindo validação justa e consistente.

Na fase de modelagem, diversos algoritmos clássicos foram avaliados: Logistic Regression, Decision Tree, Random Forest e Gradient Boosting. O conjunto de métricas (Accuracy, Precision, Recall, F1-Score e ROC AUC) permitiu uma análise quantitativa robusta. Entre todas as alternativas, o **Random Forest** apresentou o melhor equilíbrio entre robustez, interpretabilidade e desempenho.

A etapa seguinte focou na mitigação do desbalanceamento da variável-alvo. A combinação de **Class Weights** e testes com **SMOTE** reforçou a estabilidade do modelo. Embora SMOTE tenha apresentado ligeira vantagem, o uso de Class Weights se mostrou mais eficiente em termos de custo computacional, mantendo excelente desempenho geral.

Outro componente decisivo foi a análise dos **thresholds de decisão**, essencial para calibrar o comportamento final do modelo. Identificou-se que o threshold **0.55** maximiza o F1-Score e reduz falsos negativos — o erro mais crítico no contexto logístico, pois representa atrasos reais não detectados. Essa calibração confere ao modelo sensibilidade adequada para alertar a operação sem produzir excesso de alarmes falsos.

Por fim, as curvas **ROC** e **Precision–Recall** confirmaram a eficácia do modelo:

* Um ROC AUC próximo de 0.97 indica excelente capacidade discriminativa.
* A curva Precision–Recall demonstra alta estabilidade na identificação de atrasos mesmo em cenário de desbalanceamento.

Em síntese, o projeto alcançou seu objetivo principal: **construir um modelo robusto, interpretável e operacionalizável para previsão de riscos de atraso na cadeia logística da Zenatur**. O sistema é capaz de transformar dados históricos em inteligência acionável, permitindo que a empresa atue preventivamente, reduza custos e aumente a taxa de cumprimento do OTIF.

Este é um marco inicial no desenvolvimento de soluções de Data Science aplicadas à logística interna da Zenatur, abrindo caminho para automações avançadas, monitoramento contínuo e integração completa com os sistemas corporativos.

---

<div align="left">
  <a href="#topo" title="Voltar ao início do README">⬆️ Topo</a>
</div>

---