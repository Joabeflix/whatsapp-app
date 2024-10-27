



def funcao_numeros_recentes():

    lista = []

    with open('contatos_recentes.txt') as arquivos:

        for linha in arquivos:

            lista.append(linha.strip())
            print(linha.strip())

    return lista

