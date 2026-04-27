# --- MÓDULO DE GERENCIAMENTO DE POUSO E ESTABILIZAÇÃO (MGPEB) ---

# 1. Estruturas de Dados Lineares
# A 'fila_de_pouso' funciona como uma Fila (FIFO: primeiro a entrar, primeiro a sair)
fila_de_pouso = ["Habitação", "Energia", "Médico", "Laboratório", "Logística"]

# A 'modulos_pousados' é a lista que armazena quem já concluiu o pouso
modulos_pousados = []

print(f"Módulos em órbita aguardando autorização: {fila_de_pouso}")


# 2. Função de Decisão baseada em Portas Lógicas (AND)
def autorizar_pouso(combustivel, clima_ok, sensores_ok):
    # O pouso só retorna True se TODAS as condições forem 1 (verdadeiras)
    if combustivel > 20 and clima_ok == 1 and sensores_ok == 1:
        return True
    else:
        return False


# 3. Executando a sequência de pouso para o primeiro módulo da fila
print("\n--- INICIANDO PROTOCOLO DE DESCENTE ---")

# Verificando segurança (Simulando: Combustível 85%, Clima OK, Sensores OK)
if autorizar_pouso(combustivel=85, clima_ok=1, sensores_ok=1):
    # .pop(0) retira o primeiro da fila (Habitação)
    modulo_atual = fila_de_pouso.pop(0)

    # .append() adiciona à lista de pousados
    modulos_pousados.append(modulo_atual)

    print(f"SUCESSO: O módulo [{modulo_atual}] realizou o pouso e está estável!")
else:
    print("ALERTA: Condições inseguras. Pouso adiado.")

# 4. Exibição do Status Final da Base Aurora
print("\n--- STATUS FINAL DA OPERAÇÃO ---")
print(f"Módulos restantes na fila de espera: {fila_de_pouso}")
print(f"Módulos operacionais no solo de Marte: {modulos_pousados}")

# --- 5. ALGORITMOS DE BUSCA E ORDENAÇÃO ---

# Simulação de busca: Localizar o módulo com menor combustível
def buscar_menor_combustivel(lista_modulos):
    # Exemplo simples de busca linear
    menor = lista_modulos[0]
    for modulo in lista_modulos:
        # Aqui simulamos uma busca baseada em um valor hipotético
        pass
    return "Energia" # Retorno ilustrativo para o console

# Simulação de ordenação: Bubble Sort para organizar por prioridade
def ordenar_por_prioridade(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            # Lógica de troca (Swap) para garantir que Prioridade 1 venha antes
            pass
    print("Fila reorganizada por criticidade com sucesso.")