# Exercício 06 - Remover contas inativas
def remover_inativas(contas: dict[str, int], limite: int) -> dict[str, int]:
    removidas = [conta for conta, meses in contas.items() if meses > limite]

    for conta in removidas:
        del contas[conta]

    print(f"Contas removidas: {removidas}")
    print(f"Contas restantes: {contas}")

    return contas

contas_inativas = {
    "C101": 5,
    "C102": 13,
    "C103": 8,
    "C104": 15,
    "C105": 3,
    "C106": 24,
    "C107": 11
}

print("INICIANDO ROTINA DE SANEAMENTO DE CONTAS INATIVAS...")

banco_atualizado = remover_inativas(contas_inativas, 12)
