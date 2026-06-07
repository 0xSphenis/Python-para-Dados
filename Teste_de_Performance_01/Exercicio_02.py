registros = [
    ("Ana", [8, 9, 7]),
    ("Bruno", [5, 6, 5]),
    ("Carla", [10, 9, 10])
]


def processar_boletins(registros: list[tuple[str, list[int]]]) -> dict[str, list[int]]:

    notas = dict(registros)
    print(f"1. Dicionário inicial criado: {notas}")

    notas["Daniel"] = [7, 7, 8]
    print(f"2. Após a entrada do Daniel: {notas}")

    alunos_para_remover = []

    for aluno, lista_de_notas in notas.items():
        media = sum(lista_de_notas) / len(lista_de_notas)

        if media < 6:
            alunos_para_remover.append(aluno)

    for aluno in alunos_para_remover:
        del notas[aluno]
        print(f"-> Aluno '{aluno}' removido. (Média insuficiente)")

    return notas

registros_escola = [
    ("Ana", [8, 9, 7]),
    ("Bruno", [5, 6, 5]),
    ("Carla", [10, 9, 10])
]

boletins_finais = processar_boletins(registros_escola)

print(f"RESULTADO FINAL: {boletins_finais}")
