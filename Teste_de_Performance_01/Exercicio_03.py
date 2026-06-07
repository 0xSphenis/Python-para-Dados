import time

sensores_lista = [("S1", 34), ("S2", 36), ("S3", 37), ("S4", 38)]
sensores_dict = {"S1": 34, "S2": 36, "S3": 37, "S4": 38}

def comparar_desempenho(execucoes: int = 10000) -> None:

    tempos_lista = []
    tempos_dict = []

    # TESTE 1: Busca Linear na Lista
    for _ in range(execucoes):
        inicio = time.perf_counter()

        for chave, valor in sensores_lista:
            if chave == "S3":
                resultado = valor
                break

        fim = time.perf_counter()
        tempos_lista.append(fim - inicio)

    # TESTE 2: Busca Direta no Dicionário
    for _ in range(execucoes):
        inicio = time.perf_counter()
        resultado = sensores_dict["S3"]

        fim = time.perf_counter()
        tempos_dict.append(fim - inicio)

    # CÁLCULOS E RELATÓRIO
    media_lista = sum(tempos_lista) / execucoes
    media_dict = sum(tempos_dict) / execucoes

    print("# Relatório de Comparação de Desempenho")
    print(f"- Execuções: {execucoes}")
    print(f"- Tempo médio (lista): {media_lista:.6f} segundos")
    print(f"- Tempo médio (dicionário): {media_dict:.6f} segundos")

comparar_desempenho()