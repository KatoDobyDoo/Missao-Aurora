# --- MISSÃO AURORA: RELATÓRIO OPERACIONAL ---
'''
TABELA DE PARÂMETROS - MISSÃO AURORA SIGER
-----------------------------------------------------------
VARIÁVEL            | MÍNIMO  | MÁXIMO  | TIPO
-----------------------------------------------------------
temp_interna        | 15.0    | 30.0    | float
temp_externa        | -50.0   | 150.0   | float
energia             | 80.0    | 100.0   | float
pressao             | 350.0   | 480.0   | float
integridade         | 1       | 1       | boolean (0/1)
sistemas_criticos   | 1       | 1       | boolean (0/1)
-----------------------------------------------------------
'''

print("--- SISTEMA DE TELEMETRIA AURORA ---")

# 1. Entrada de Dados (O programa para e espera você digitar)
temp_interna = float(input("Digite a Temperatura Interna (°C): "))
temp_externa = float(input("Digite a Temperatura Externa (°C): "))
integridade = int(input("Integridade Estrutural (1-OK / 0-FALHA): "))
energia = float(input("Nível de Energia (%): "))
pressao = float(input("Pressão dos Tanques (PSI): "))
modulos = int(input("Status dos Módulos Críticos (1-OK / 0-FALHA): "))

# Agora abaixo viria o seu código de inputs e ifs...

# 2. Lógica de Verificação (Usando os limites pré estabelecidos)
# O Python vai testar cada condição e guardar True ou False
temp_ok = (15 <= temp_interna <= 30) and (-50 <= temp_externa <= 150)
energia_ok = energia >= 80
pressao_ok = 350 <= pressao <= 480
sistemas_ok = (integridade == 1) and (modulos == 1)

print("\n--- PROCESSANDO RESULTADOS ---")

# 3. Decisão Final (O "Cérebro" do código)
if temp_ok and energia_ok and pressao_ok and sistemas_ok:
    print("STATUS: >>>> PRONTO PARA DECOLAR <<<<")
    print("Sistemas em conformidade. Boa viagem, Aurora!")
else:
    print("STATUS: >>>> DECOLAGEM ABORTADA <<<<")
    print("Motivos da falha:")

    # Verificando qual item específico causou o erro
    if not temp_ok:
        print("- Temperatura fora da faixa de segurança.")
    if not energia_ok:
        print("- Nível de energia insuficiente (mínimo 80%).")
    if not pressao_ok:
        print("- Pressão dos tanques instável.")
    if not sistemas_ok:
        print("- Falha crítica na estrutura ou módulos.")