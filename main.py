import csv

from pygres_connection import db

from pessoa import insere_pessoa
from pessoa import retorna_pessoas
from pessoa import retorna_pessoa
from pessoa import atualiza_pessoa
from pessoa import remove_pessoa


def ler_arquivo():
    with open('curso-mvcad.csv', encoding="utf8") as file:
        leitor = csv.DictReader(file, delimiter=',')

        for pessoa in leitor:
            #print(pessoa) para visualisar aqui
            cpf = pessoa['cpf'].replace('.','')
            pessoa['cpf'] = cpf.replace('-', '')
            insere_pessoa(pessoa)

#ler_arquivo()
#print(retorna_pessoas())

#pessoa = {
    #'nome' : 'Eduardo',
    #'endereco' : 'Rua Benedicto',
    #'cpf' : '38025278875',
    #'estado': 'São Paulo',
    #'turma':'Mvcad Cobol',
    #'periodo':'noturno',
    #'modulo': 'Sexto módulo'
#}

#pessoa = retorna_pessoa(2)
#pessoa['cpf'] = "17626466845"
#atualiza_pessoa(pessoa)
#retorna_pessoas
#insere_pessoa(pessoa)
#remove_pessoa(3)
#print(retorna_pessoa(2))


