# Exercício 05 - operações entre conjuntos de clientes
def obter_em_todas(c1: set, c2: set, c3: set) -> set:
    return c1 & c2 & c3

def obter_em_pelo_menos_duas(c1: set, c2: set, c3: set) -> set:
    return (c1 & c2) | (c1 & c3) | (c2 & c3)

def obter_exclusivos(alvo: set, outras1: set, outras2: set) -> set:
    return alvo - (outras1 | outras2)

def obter_total_unicos(c1: set, c2: set, c3: set) -> int:
    return len(c1 | c2 | c3)

def formatar_set(conjunto: set) -> str:
    return "{" + ", ".join(map(str, sorted(conjunto))) + "}"

campanha_credito_rapido = {1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1010, 1012}
campanha_invest_plus = {1005, 1006, 1009, 1010, 1011, 1012, 1013, 1014}
campanha_cashback_fidelidade = {1001, 1003, 1005, 1011, 1015, 1016, 1017, 1018}

em_todas = obter_em_todas(campanha_credito_rapido, campanha_invest_plus, campanha_cashback_fidelidade)

em_pelo_menos_duas = obter_em_pelo_menos_duas(campanha_credito_rapido, campanha_invest_plus, campanha_cashback_fidelidade)

exclusivos_credito = obter_exclusivos(campanha_credito_rapido, campanha_invest_plus, campanha_cashback_fidelidade)
exclusivos_invest = obter_exclusivos(campanha_invest_plus, campanha_credito_rapido, campanha_cashback_fidelidade)
exclusivos_cashback = obter_exclusivos(campanha_cashback_fidelidade, campanha_credito_rapido, campanha_invest_plus)

total_clientes = obter_total_unicos(campanha_credito_rapido, campanha_invest_plus, campanha_cashback_fidelidade)

print(f"Clientes em todas as campanhas: {formatar_set(em_todas)}")
print(f"Clientes em pelo menos duas campanhas: {formatar_set(em_pelo_menos_duas)}")
print("Clientes exclusivos:")
print(f"- Crédito Rápido: {formatar_set(exclusivos_credito)}")
print(f"- Invest+: {formatar_set(exclusivos_invest)}")
print(f"- Cashback Fidelidade: {formatar_set(exclusivos_cashback)}")
print(f"Total de clientes únicos: {total_clientes}")