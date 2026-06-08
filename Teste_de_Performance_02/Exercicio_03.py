# Exercício 3 Comparar tempo de busca entre lista e dicionário
import time

def calcular_media(valores: list[float]) -> float:
    if not valores:
        return 0.0
    return sum(valores) / len(valores)

def simular_benchmark_cache(execucoes: int = 10000) -> None:
    sensores_lista = [("S1", 34), ("S2", 36), ("S3", 37), ("S4", 38)]
    sensores_dict = {"S1": 34, "S2": 36, "S3": 37, "S4": 38}

    tempos_lista = []
    tempos_dict = []

    for _ in range(execucoes):
        inicio = time.perf_counter()

        for chave, valor in sensores_lista:
            if chave == "S3":
                resultado = valor
                break

        fim = time.perf_counter()
        tempos_lista.append(fim - inicio)

    for _ in range(execucoes):
        inicio = time.perf_counter()

        resultado = sensores_dict["S3"]

        fim = time.perf_counter()
        tempos_dict.append(fim - inicio)

    media_lista = calcular_media(tempos_lista)
    media_dict = calcular_media(tempos_dict)

    print("⚡ RELATÓRIO DE PERFORMANCE DE CACHE (SJ90) ⚡")
    print("-" * 55)
    print(f"-> Total de consultas simuladas: {execucoes}")
    print(f"-> Tempo médio (Lista de Tuplas): {media_lista:.8f} segundos")
    print(f"-> Tempo médio (Dicionário)     : {media_dict:.8f} segundos")

    if media_dict > 0:
        aceleracao = media_lista / media_dict
        print(f"Conclusão: O Dicionário foi aprox. {aceleracao:.0f}x mais rápido.")


simular_benchmark_cache()