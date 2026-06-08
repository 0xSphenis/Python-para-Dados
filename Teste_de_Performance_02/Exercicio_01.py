# Exercício 01 - Cadastro Inicial de Clientes

base_clientes = {
    501: {"nome": "Ana Costa", "cidade": "Rio de Janeiro", "saldo": 1250.75},
    502: {"nome": "Bruno Lima", "cidade": "São Paulo", "saldo": 980.40},
    503: {"nome": "Carla Nunes", "cidade": "Belo Horizonte", "saldo": 870.30},
    504: {"nome": "Diego Santos", "cidade": "Curitiba", "saldo": -10.00},
    505: {"nome": "Elaine Martins", "cidade": "Recife", "saldo": 1530.25}
}

def atualizar_clientes(clientes: dict[int, dict], id_cliente: int, nome: str, cidade: str, saldo: float) -> dict[
    int, dict]:

    if saldo < 0:
        if id_cliente in clientes:
            del clientes[id_cliente]
            print(f"[-] CONTA ENCERRADA: Cliente {id_cliente} ({nome}) removido por saldo negativo (R$ {saldo:.2f}).")
        else:
            print(f"[!] CADASTRO RECUSADO: '{nome}' tentou abrir conta com saldo negativo.")

    else:
        clientes[id_cliente] = {
            "nome": nome,
            "cidade": cidade,
            "saldo": saldo
        }
        print(f"[+] SUCESSO: Cadastro do cliente {id_cliente} ({nome}) processado.")

    return clientes


print("INICIANDO PROCESSAMENTO DE ONBOARDING...")

# 1. Novo cliente – deve ser adicionado
atualizar_clientes(base_clientes, 506, "Fábio Mendes", "Fortaleza", 720.00)

# 2. Cliente existente – deve ter saldo atualizado
atualizar_clientes(base_clientes, 502, "Bruno Lima", "São Paulo", 1180.90)

# 3. Cliente com saldo negativo – deve ser removido
atualizar_clientes(base_clientes, 504, "Diego Santos", "Curitiba", -50.00)

print("\nRELATÓRIO FINAL DA BASE LOCAL (PRONTO PARA API)")
for id_cliente, dados in base_clientes.items():
    print(
        f"ID: {id_cliente} | Nome: {dados['nome'].ljust(15)} | Cidade: {dados['cidade'].ljust(16)} | Saldo: R$ {dados['saldo']:.2f}")
