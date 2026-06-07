def gerenciar_configuracao(dados_config: dict, nome_arquivo: str = "config.txt") -> None:
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for chave, valor in dados_config.items():
            arquivo.write(f"{chave}={valor}\n")

    print(f"Arquivo '{nome_arquivo}' gerado e salvo com sucesso no disco!\n")

    print("🖥LENDO CONFIGURAÇÕES DO SISTEMA (AUDITORIA):")

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()

        print(conteudo, end="")

config = {
    "servidor": "192.168.0.10",
    "porta": 8080,
    "modo": "produção"
}

gerenciar_configuracao(config)