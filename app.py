import numpy as np
from flask import Flask, jsonify, request
from flask_restx import Api, Resource,fields
from utils.classificador import classificador_palavras
from array import array

app  = Flask(__name__)

app_infos = dict(version='1.0', title='Classificador de palavras',
        description='Análise de uma frase aleatória')

rest_app = Api(app, **app_infos)

db_model = rest_app.model('Variáveis usadas no primeiro modelo', 
	{'array': fields.List(cls_or_instance= fields.String ,required = True, 
					 description="String que contem um array: 1,9,8", 
					 help="Ex. 1,9,8")})

# fazendo um teste de get 
nome_do_endpoint = rest_app.namespace('teste_get', description='Teste de Get')
@nome_do_endpoint.route("/classificador")
class classify(Resource):
    @rest_app.expect(db_model)
    def post(self):
        string = request.json['array']
        string = string[0]
        classifica = classificador_palavras().classificador(string)
        return(classifica)

@app.route("/segundo_endpoint/<int:array_do_usuario>")
def segundo_endpoint(array_do_usuario):
  array_do_usuario = np.array([array_do_usuario])
  return (f"Sua solicitação foi: {array_do_usuario}", 200)


if __name__ == "__main__":
  debug = True 
  app.run(host='0.0.0.0', port=7000, debug=debug) # porta 
