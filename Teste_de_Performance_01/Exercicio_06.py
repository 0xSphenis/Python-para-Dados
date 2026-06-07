from datetime import date

estoque_medicamentos = {
    "Aspirina": "2024-11-01",
    "Dipirona": "2026-03-10",
    "Paracetamol": "2023-12-01"
}

def filtrar_vencidos(medicamentos_dict: dict[str, str]) -> dict[str, str]:

    hoje = date.today()

    produtos_validos = {
        nome: data_str
        for nome, data_str in medicamentos_dict.items()
        if date.fromisoformat(data_str) >= hoje
    }

    total_removidos = len(medicamentos_dict) - len(produtos_validos)

    print("RELATÓRIO DE AUDITORIA SANITÁRIA")
    print(f"Data da Auditoria: {hoje.strftime('%d/%m/%Y')}")
    print(f"Medicamentos inspecionados: {len(medicamentos_dict)}")
    print(f"Total de itens vencidos removidos: {total_removidos}")

    return produtos_validos

print(f"Estoque Inicial: {estoque_medicamentos}\n")

estoque_limpo = filtrar_vencidos(estoque_medicamentos)

print(f"Estoque Final Atualizado: {estoque_limpo}")