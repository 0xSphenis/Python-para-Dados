from collections import Counter
import os

conteudo_inicial = """Python é poderoso e versátil.
Python permite automação e análise.
Automação é essencial em engenharia."""

with open("relatorio.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(conteudo_inicial)


def analisar_palavras_frequentes(caminho_arquivo: str) -> list[tuple[str, int]]:

    contador = Counter()

    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha_limpa = linha.lower()

            pontuacoes = [".", ",", "!", "?", ";", ":"]
            for pontuacao in pontuacoes:
                linha_limpa = linha_limpa.replace(pontuacao, "")

            palavras = linha_limpa.split()

            contador.update(palavras)

    top_3 = contador.most_common(3)

    return top_3

print("RELATÓRIO DE FREQUÊNCIA TEXTUAL")

resultado = analisar_palavras_frequentes("relatorio.txt")

for posicao, (palavra, quantidade) in enumerate(resultado, start=1):
    print(f"{posicao}º Lugar | '{palavra}': {quantidade} ocorrência(s)")