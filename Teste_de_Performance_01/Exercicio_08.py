clientes_A = {"Ana", "Bruno", "Carla", "Daniel"}
clientes_B = {"Bruno", "Carla", "Eduardo", "Fernanda"}

def analisar_bases_crm(base_a: set[str], base_b: set[str]) -> None:

    comuns = base_a.intersection(base_b)

    exclusivos_a = base_a.difference(base_b)
    exclusivos_b = base_b.difference(base_a)

    todos_unicos = base_a.union(base_b)

    print("RELATÓRIO DE CONSOLIDAÇÃO DE CLIENTES (CRM)")
    print(f"🔹 Clientes em ambas as bases (Interseção) : {comuns}")
    print(f"🔹 Clientes exclusivos Base A (Diferença)   : {exclusivos_a}")
    print(f"🔹 Clientes exclusivos Base B (Diferença)   : {exclusivos_b}")
    print(f"🔹 Base consolidada completa (União)        : {todos_unicos}")

    print(f"Total de clientes únicos no sistema: {len(todos_unicos)}")


analisar_bases_crm(clientes_A, clientes_B)