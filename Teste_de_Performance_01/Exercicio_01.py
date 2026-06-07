# EXERCÍCIO 01
estoque = {
    "Python Crash Course": 4,
    "Clean Code": 2,
    "Automate the Boring Stuff": 0
}

def atualizar_estoque(estoque: dict[str, int], livro: str, quantidade: int) -> dict[str, int]:
    estoque_atual = estoque.get(livro, 0) #usa metodo get para verificar se livro existe no sist.
    nova_quantidade = estoque_atual + quantidade  #atualiza a quantidade

    if nova_quantidade < 0: #avisa o usuário que a quantidade retirada é maior que o estoque ("regra de negócio")
        print(f"Erro, a tentativa de retirar '{livro}' ultrapassou o estoque máximo")

    elif nova_quantidade == 0: #caso a quantidad chegue a zero, remove conforme enunciado da questão
        if livro in estoque:
            del estoque[livro]
            print(f"livro {livro} zerou e foi removido do sistema de estoque")

    else: #se o caso for adicionar livros, atualiza a quantidade em estoque
        estoque[livro] = nova_quantidade
    print(f"Estoque após alteração {livro}: {quantidade}")

    return estoque

print(f"Estoque Inicial: {estoque}\n")

# Tentativas de atualização pedidas no moodle
atualizar_estoque(estoque, "Clean Code", 3)
atualizar_estoque(estoque, "Fluent Python", 5)
atualizar_estoque(estoque, "Automate the Boring Stuff", 0)

print(f"\n{estoque}")



