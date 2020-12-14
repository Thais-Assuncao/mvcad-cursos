from pygres_connection import db


def insere_pessoa(dados_pessoa):
    db.insert("pessoa", nome=dados_pessoa['nome'],
              endereco=dados_pessoa['endereco'],
              cpf=dados_pessoa['cpf'],
              estado=dados_pessoa['estado'],
              turma=dados_pessoa['turma'],
              periodo=dados_pessoa['periodo'],
              modulo=dados_pessoa['modulo'])

def retorna_pessoas():
    query = db.query("SELECT * FROM pessoa")
    return query.dictresult() if query else {}

def retorna_pessoa(id):
    query = db.query_formatted("SELECT * FROM pessoa WHERE id = %s", [id])
    return query.singledict() if query else {}
#if query = se tiver valor retorna o valor else retorna um dicionario vazio

def atualiza_pessoa(pessoa):
    db.update("pessoa", pessoa)

def remove_pessoa(id):
    db.query_formatted("DELETE FROM pessoa WHERE id = %s", [id])
#  %s é o parâmetro

