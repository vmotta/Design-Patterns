def imprime(nota_fiscal) -> None:
    print(f" Imprimindo a nota fiscal {nota_fiscal.cnpj}")


def envia_por_email(nota_fiscal) -> None:
    print(f" Enviando a nota fiscal por email {nota_fiscal.cnpj}")


def salva_no_banco(nota_fiscal) -> None:
    print(f" Salvando a nota fiscal {nota_fiscal.cnpj}")
