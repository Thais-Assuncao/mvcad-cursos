from flask import Flask, request
from flask_restful import Resource, Api

from pessoa import retorna_pessoas, atualiza_pessoa
from pessoa import insere_pessoa, retorna_pessoa, remove_pessoa


app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource): #resource são todos os métodos de api que podemos ter
    def get(self):
        return "Uhuuuuuuuuuul"


class Pessoa(Resource): # significa que a Pessoa herda o que a classe Resource tem
    def get(self):
        pessoas = retorna_pessoas()
        return pessoas

    def post(self):
        pessoa = request.json
        insere_pessoa(pessoa)
        return "Pessoa inserida com sucesso!"

    def put(self): #atualiza
        pessoa = request.json
        atualiza_pessoa(pessoa)
        return "Pessoa atualizada com sucesso!"

class PessoaDatail(Resource):
    def get(self, id):
        pessoa = retorna_pessoa(id)
        return pessoa

    def delete(self, id):
        remove_pessoa(id)
        return "Pessoa removida com sucesso!"

api.add_resource(HelloWorld, "/") #a / é o endpoint
api.add_resource(Pessoa, "/pessoas")
api.add_resource(PessoaDatail, "/pessoa/<int:id>")


if __name__ == "__main__":
    app.run(debug=True)



