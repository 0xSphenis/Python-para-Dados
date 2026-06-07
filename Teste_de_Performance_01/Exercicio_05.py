temperaturas = {
    "RJ": 29.4,
    "SP": -99.0,
    "MG": 27.2,
    "BA": 31.1,
    "RS": -88.0
}

def filtrar_temperaturas(temp_dict: dict[str, float]) -> dict[str, float]:

    temperaturas_limpas = {
        estacao: temp
        for estacao, temp in temp_dict.items()
        if temp >= -50
    }

    total_original = len(temp_dict)
    total_novo = len(temperaturas_limpas)
    entradas_removidas = total_original - total_novo

    print("RELATÓRIO DE LIMPEZA CLIMÁTICA")
    print(f"-> Leituras inválidas removidas: {entradas_removidas}")
    print(f"-> Estações válidas restantes: {total_novo}")

    return temperaturas_limpas


print(f"Dicionário original: {temperaturas}\n")

temperaturas_validadas = filtrar_temperaturas(temperaturas)

print(f"\nDicionário final validado:\n{temperaturas_validadas}")