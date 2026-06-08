# Exercício 04 - Detectar CPFs duplicados
def auditar_cpfs_compliance(cpfs_brutos: list[str]) -> None:
    cpfs_unicos = set(cpfs_brutos)

    vistos = set()
    cpfs_repetidos = set()

    for cpf in cpfs_brutos:
        if cpf in vistos:
            cpfs_repetidos.add(cpf)
        else:
            vistos.add(cpf)

    total_original = len(cpfs_brutos)
    total_unico = len(cpfs_unicos)

    cadastros_redundantes = total_original - total_unico

    print("RELATÓRIO DE COMPLIANCE E INTEGRIDADE DE DADOS")
    print(f"Total de registros recebidos : {total_original}")
    print(f"Total de CPFs únicos válidos : {total_unico}")
    print(f"Cadastros redundantes barrados: {cadastros_redundantes}")

    print("\nALERTA: Os seguintes CPFs apresentaram duplicidade na importação:")
    for cpf_suspeito in sorted(cpfs_repetidos):
        cpf_formatado = f"{cpf_suspeito[:3]}.{cpf_suspeito[3:6]}.{cpf_suspeito[6:9]}-{cpf_suspeito[9:]}"
        print(f" -> {cpf_formatado}")

cpfs_importados = [
    "12345678900", "98765432100", "11122233344", "55566677788",
    "12345678900", "98765432100", "22233344455", "33344455566",
    "44455566677", "55566677788", "66677788899", "77788899900",
    "88899900011", "99900011122", "11122233344", "12312312312",
    "23423423423", "34534534534", "45645645645", "56756756756",
    "67867867867", "78978978978", "89089089089", "90190190190",
    "98765432100", "55566677788", "44455566677", "44455566677"
]

auditar_cpfs_compliance(cpfs_importados)