# Exercício 07 -  Registrar extratos em um arquivo
def processar_extratos_diarios(transacoes_dict: dict[str, list[float]], nome_arquivo: str = "extrato_sj90.txt") -> None:

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for cliente, lista_transacoes in transacoes_dict.items():
            linha_formatada = f"Cliente: {cliente} | Transações: {lista_transacoes}\n"
            arquivo.write(linha_formatada)

    print(f"SUCESSO: Arquivo '{nome_arquivo}' gerado e salvo no disco rígido.\n")
    print("LENDO DADOS DO ARQUIVO PARA AUDITORIA:")

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()

        print(conteudo.strip())

transacoes = {
    "Ana Costa": [250.0, -100.0, 320.0],
    "Bruno Lima": [-50.0, 400.0, -10.0]
}

processar_extratos_diarios(transacoes)