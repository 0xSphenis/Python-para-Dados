# Exercício 02 - Agrupar contas por agência
contas = [
    ("001-RJ", "Ana Costa", 1250.75),
    ("001-RJ", "Bruno Lima", 980.40),
    ("002-SP", "Carla Nunes", 870.30),
    ("002-SP", "Daniel Souza", 1150.10)
]

def agrupar_por_agencia(contas_planas: list[tuple[str, str, float]]) -> dict[str, dict[str, float]]:

    contas_agrupadas = {}

    for agencia, cliente, saldo in contas_planas:

        if agencia not in contas_agrupadas:
            contas_agrupadas[agencia] = {}

        contas_agrupadas[agencia][cliente] = saldo

    print("RELATÓRIO CONSOLIDADO POR UNIDADE DE ATENDIMENTO")

    for agencia, dicionario_clientes in contas_agrupadas.items():
        total_clientes = len(dicionario_clientes)
        print(f"-> Agência: {agencia} | Total de clientes vinculados: {total_clientes}")


    return contas_agrupadas

dicionario_final = agrupar_por_agencia(contas)

print("\n[Estrutura de Dados Gerada]:")
print(dicionario_final)