emails = [
    "ana@empresa.com",
    "bruno@empresa.com",
    "ana@empresa.com",
    "carla@empresa.com",
    "bruno@empresa.com",
    "daniel@empresa.com"
]

def limpar_lista_emails(emails_brutos: list[str]) -> list[str]:

    total_inicial = len(emails_brutos)

    emails_unicos = sorted(set(emails_brutos))

    total_final = len(emails_unicos)
    duplicatas_removidas = total_inicial - total_final

    print("RELATÓRIO DE HIGIENIZAÇÃO DE LEADS")
    print(f"Total inicial de e-mails: {total_inicial}")
    print(f"Duplicatas removidas: {duplicatas_removidas}")
    print(f"Total de e-mails únicos: {total_final}")

    return emails_unicos


lista_final = limpar_lista_emails(emails)

print("Lista final pronta para disparo (Ordenada):")
for email in lista_final:
    print(f"-> {email}")