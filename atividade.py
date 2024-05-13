import re
import csv

def extrair_contatos(texto):
    padrao_nome = re.compile(r'Nome: (\w+)\s')
    padrao_telefone = re.compile(r'Telefone: (\(\d{2}\)\s\d{5}-\d{4})\s')
    padrao_email = re.compile(r'E-mail: (\w+@\w+\.\w+)')
    dados = []
    for item in padrao_nome.finditer(texto):
        nome = item.group(1)
        tell = padrao_telefone.search(texto, item.end())
        telefone = tell.group(1)
        email = padrao_email.search(texto, tell.end())
        email = email.group(1)
        dados.append((nome, telefone, email))
    return dados

def gerar_csv(contatos, nome_arquivo):
    cabecalho = ['Nome', 'Telefone', 'Email']

    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(cabecalho)
        escritor.writerows(contatos)


texto_contatos = """
    Nome: João Silva
    Telefone: (63)98456-7890
    E-mail: joao@gmail.com
    
    Nome: Maria Santos
    Telefone: (63)98789-0123
    E-mail: maria@gmail.com
    
    Nome: Pedro Almeida
    Telefone: (62)98312-3456
    E-mail: pedro@gmail.com
    """

contatos = extrair_contatos(texto_contatos)
print (contatos)
gerar_csv(contatos, 'contatos.csv')

