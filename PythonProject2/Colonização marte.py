#  SISTEMA INTEGRADO DE OPERAÇÃO CONTÍNUA (AURORA CENTRAL)

# 1. ORGANIZAÇÃO DOS DADOS
colonia_dados = {
    "sistema_energetico": {
        "geracao_solar": 45,        # em kW
        "geracao_eolica": 25,       # em kW
        "consumo_total": 60,        # em kW
        "reserva_baterias": 80      # em %
    },
    "sistema_ambiental": {
        "temperatura_interna": 22,  # em °C
        "temperatura_externa": -55, # em °C
        "pressao_interna": 101.3    # em kPa
    },
    "sistema_operacional": {
        "velocidade_vento": 12,     # em m/s
        "status_suporte_vida": 1,   # 1 = Ligado, 0 = Desligado
        "status_laboratorio": 1,    # 1 = Ligado, 0 = Desligado
        "status_logistica": 1       # 1 = Ligado, 0 = Desligado
    }
}

# 2. REGRAS DE DECISÃO AUTOMÁTICAS

def analisar_uso_energia(geracao_solar, geracao_eolica, consumo):
    # Calcula a geração total combinando as duas fontes
    geracao_total = geracao_solar + geracao_eolica

    print(f"Geração Total: {geracao_total}kW | Consumo Atual: {consumo}kW")

    # Regra Lógica: Se o consumo for maior que a geração -> Risco
    if consumo > geracao_total:
        return "ALERTA: Consumo maior que geração. Reduzir carga imediatamente!"
    else:
        return "SUGESTÃO: Geração estável. Armazenar energia excedente nas baterias."


def gerenciar_sistemas_criticos(reserva_baterias, consumo, tendencia_clima_ruim=False):
    # Regra Lógica Avançada: Energia Baixa AND Consumo Alto AND Clima Desfavorável
    if reserva_baterias < 50 and consumo > 50 and tendencia_clima_ruim:
        # Prioriza o suporte à vida e desliga sistemas não essenciais
        status_suporte = "LIGADO (Prioridade Máxima)"
        status_lab = "DESLIGADO (Modo de Economia Crítico)"
        status_logistica = "DESLIGADO (Modo de Economia Crítico)"

        print("\n--- PROTOCOLO DE EMERGÊNCIA ATIVADO ---")
        print(f"Suporte à Vida: {status_suporte}")
        print(f"Laboratório Científico: {status_lab}")
        print(f"Módulo de Logística: {status_logistica}")
        return "ALERTA CRÍTICO: Modo de economia extrema ativado devido ao clima e baixa reserva!"

    return "Sistemas operando dentro das margens normais de segurança."


# 3. PREVER COMPORTAMENTOS SIMPLES (Regressão Linear Manual)

def treinar_previsao_eolica():
    # Dados históricos fornecidos pelo enunciado
    historico_vento = [8, 10, 12]  # velocidade do vento em m/s (X)
    historico_energia = [20, 25, 30]  # energia gerada em kW (Y)

    # Passo 1: Calcular as médias de X e Y
    media_x = sum(historico_vento) / len(historico_vento)
    media_y = sum(historico_energia) / len(historico_energia)

    # Passo 2: Calcular os componentes para a inclinação da reta (m)
    # Fórmula: m = somatorio((x - media_x) * (y - media_y)) / somatorio((x - media_x)^2)
    numerador = 0
    denominador = 0

    for i in range(len(historico_vento)):
        diff_x = historico_vento[i] - media_x
        diff_y = historico_energia[i] - media_y
        numerador += diff_x * diff_y
        denominador += diff_x ** 2

    inclinacao_m = numerador / denominador

    # Passo 3: Calcular o ponto de interseção (b) -> b = media_y - (m * media_x)
    intersecao_b = media_y - (inclinacao_m * media_x)

    return inclinacao_m, intersecao_b


def prever_energia_futura(novo_vento):
    # Obtém os parâmetros da reta calculados pelo histórico
    m, b = treinar_previsao_eolica()

    # Aplica a equação da reta: y = m * x + b
    energia_estimada = (m * novo_vento) + b
    return energia_estimada


# --- 4. FLUXO PRINCIPAL DE EXECUÇÃO (TESTE DO SISTEMA) ---
if __name__ == "__main__":
    print("=== MONITORAMENTO CENTRAL DA COLÔNIA AURORA ===")

    # Testando a análise de energia atual
    print("\n[Fase de Análise Atual]")
    solar = colonia_dados["sistema_energetico"]["geracao_solar"]
    eolica = colonia_dados["sistema_energetico"]["geracao_eolica"]
    consumo = colonia_dados["sistema_energetico"]["consumo_total"]

    resultado_analise = analisar_uso_energia(solar, eolica, consumo)
    print(resultado_analise)

    # Testando o modelo de previsão por regressão
    print("\n[Fase de Estimativa Futura]")
    vento_simulado = 11
    previsao = prever_energia_futura(vento_simulado)
    print(f"Entrada (Velocidade do Vento Projetada): {vento_simulado} m/s")
    print(f"Saída (Previsão de Geração Eólica): {previsao:.1f} kW")

    # Testando o protocolo de emergência (combinando critérios)
    bateria = colonia_dados["sistema_energetico"]["reserva_baterias"]
    # Simulando um cenário crítico externo
    alertas = gerenciar_sistemas_criticos(reserva_baterias=40, consumo=70, tendencia_clima_ruim=True)
    print(alertas)