medias = {"Ana": 8.5, "Bruno": 6.3, "Carla": 9.1}

def gerar_ranking_alunos(medias: dict[str, float]) -> list[tuple[str, float]]:

    lista_tabular = list(medias.items())

    ranking = sorted(lista_tabular, key=lambda item: item[1], reverse=True)

    print(" RANKING ACADÊMICO ")

    for posicao, (aluno, nota) in enumerate(ranking, start=1):
        print(f"{posicao}º Lugar | Aluno(a): {aluno.ljust(10)} | Média: {nota}")

    return ranking


medias_turma = {
    "Ana": 8.5,
    "Bruno": 6.3,
    "Carla": 9.1
}

relatorio_final = gerar_ranking_alunos(medias_turma)

print(f"\n[Formato Técnico para Exportação]:\n{relatorio_final}")