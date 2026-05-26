# Sistema Integrado de Operação Contínua (Aurora Central)

Este repositório contém o módulo computacional central desenvolvido para a fase de operação contínua da colônia **Aurora Siger**, como parte da Atividade Integradora do curso de Ciência da Computação. O sistema evoluiu de um modelo puramente reativo para um sistema inteligente, capaz de organizar dados de sensores em tempo real, aplicar regras lógicas de decisão e prever a geração de recursos futuros por meio de regressão linear.

## Funcionamento do Sistema

O software atua como o cérebro da infraestrutura marciana, processando variáveis críticas distribuídas por toda a base. Ele é estruturado em três pilares fundamentais:

1. **Organização Hierárquica (Chave-Valor):** Os dados coletados pelos sensores de superfície são agrupados dinamicamente em dicionários estruturados. Isso divide a base em subsistemas específicos (Energético, Ambiental e Operacional) para garantir acesso instantâneo às informações.
2. **Lógica de Decisão Automatizada:** Utilizando expressões booleanas compostas (`AND`, `OR`), o sistema analisa o balanço entre consumo e geração, ativando automaticamente protocolos de economia e gerenciando o desligamento de módulos não essenciais (como Laboratório e Logística) para proteger o Suporte à Vida em cenários críticos.
3. **Predição Inteligente por Regressão:** O algoritmo utiliza séries de dados históricos de velocidade do vento para calcular os coeficientes da reta operacional de forma manual, eliminando dependências externas e prevendo quanta energia eólica estará disponível para a colônia diante de novas condições climáticas.

---

## Exemplos de Entrada e Saída

O fluxo clássico de entrada, processamento e saída do protótipo gera as seguintes respostas no console de monitoramento:

### 1. Análise Energética Atual
* **Entrada (Dados do Dicionário):** * Geração Solar: `45 kW`
  * Geração Eólica: `25 kW`
  * Consumo Total: `60 kW`
* **Saída do Sistema:** ```text
  Geração Total: 70kW | Consumo Atual: 60kW
  SUGESTÃO: Geração estável. Armazenar energia excedente nas baterias.

  Entrada (Velocidade do Vento Projetada): 11 m/s
Saída (Previsão de Geração Eólica): 27.5 kW

--- PROTOCOLO DE EMERGÊNCIA ATIVADO ---
Suporte à Vida: LIGADO (Prioridade Máxima)
Laboratório Científico: DESLIGADO (Modo de Economia Crítico)
Módulo de Logística: DESLIGADO (Modo de Economia Crítico)
ALERTA CRÍTICO: Modo de economia extrema ativado devido ao clima e baixa reserva!
