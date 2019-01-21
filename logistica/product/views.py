from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from logistica import db, app
from logistica.product.models import User

catalog = Blueprint('product', __name__)

@catalog.route('/')
@catalog.route('/home')
def home():
    return "Bem vindo aa API do truckpad"

class ProductView(MethodView):

    def post(self):
        nome = request.get_json().get('nome')
        sexo = request.get_json().get('sexo')
        tipoVeiculo = request.get_json().get('tipoVeiculo')
        veiculoCarregado = request.get_json().get('veiculoCarregado')
        idade = request.get_json().get('idade')
        cnh = request.get_json().get('cnh')
        possuiVeiculo = request.get_json().get('possuiVeiculo')
        cepOrigem = request.get_json().get('cepOrigem')
        cepDestino = request.get_json().get('cepDestino')

        user = User(nome, sexo, tipoVeiculo, veiculoCarregado, idade, cnh, possuiVeiculo, cepOrigem, cepDestino)
        db.session.add(user)
        db.session.commit()
        return jsonify({user.id: {
            'nome': user.nome,
            'sexo': user.sexo,
            'tipoVeiculo': user.tipoVeiculo,
            'veiculoCarregado': user.veiculoCarregado,
            'idade': user.idade,
            'cnh': user.cnh,
            'possuiVeiculo': user.possuiVeiculo,
            'cepOrigem': user.cepOrigem,
            'cepDestino': user.cepDestino
        }})

    def get(self, id=None, page=1):
        if not id:
            products = User.query.paginate(page, 10).items
            res = {}
            for product in products:
                res[product.id] = {
                    'nome': product.nome,
                    'sexo': product.sexo,
                    'tipoVeiculo': product.tipoVeiculo,
                    'veiculoCarregado': product.veiculoCarregado,
                    'idade': product.idade,
                    'cnh': product.cnh,
                    'possuiVeiculo': product.possuiVeiculo,
                    'cepOrigem': product.cepOrigem,
                    'cepDestino': product.cepDestino
                }
        else:
            product = User.query.filter_by(id=id).first()
            if not product:
                abort(404)
            res = {
                'name': product.nome,
                'sexo': product.sexo,
                'tipoVeiculo': product.tipoVeiculo,
                'veiculoCarregado': product.veiculoCarregado,
                'idade': product.idade,
                'cnh': product.cnh,
                'possuiVeiculo': product.possuiVeiculo,
                'cepOrigem': product.cepOrigem,
                'cepDestino': product.cepDestino
            }
        return jsonify(res)

    def put(self, id):
        # Update the record for the provided id
        # with the details provided.
        user = User.query.get(id)

        if user is not None:
            user.nome = request.get_json().get('nome')
            user.sexo = request.get_json().get('sexo')
            user.tipoVeiculo = request.get_json().get('tipoVeiculo')
            user.veiculoCarregado = request.get_json().get('veiculoCarregado')
            user.idade = request.get_json().get('idade')
            user.cnh = request.get_json().get('cnh')
            user.possuiVeiculo = request.get_json().get('possuiVeiculo')
            user.cepOrigem = request.get_json().get('cepOrigem')
            user.cepDestino = request.get_json().get('cepDestino')

            db.session.commit()
            return jsonify({user.id: {
                'nome': user.nome,
                'sexo': user.sexo,
                'tipoVeiculo': user.tipoVeiculo,
                'veiculoCarregado': user.veiculoCarregado,
                'idade': user.idade,
                'cnh': user.cnh,
                'possuiVeiculo': user.possuiVeiculo,
                'cepOrigem': user.cepOrigem,
                'cepDestino': user.cepDestino
            }})
        return ""

    def delete(self, id):
        # Delete the record for the provided id.
        obj = User.query.filter_by(id=id).one()
        db.session.delete(obj)
        db.session.commit()
        return "Usuario deletado com sucesso"

    @app.route('/user-noload', methods=['GET'])
    def usernoload(page=1):
        products = User.query.paginate(page, 10).items
        res = {}
        for product in products:
            if (product.veiculoCarregado == "False"):
                res[product.id] = {
                'nome': product.nome,
                'sexo': product.sexo,
                'tipoVeiculo': product.tipoVeiculo,
                'veiculoCarregado': product.veiculoCarregado,
                'idade': product.idade,
                'cnh': product.cnh,
                'possuiVeiculo': product.possuiVeiculo,
                'cepOrigem': product.cepOrigem,
                'cepDestino': product.cepDestino
            }
        return jsonify(res)

    @app.route('/own-vehicle', methods=['GET'])
    def uservehicle(page=1):
        products = User.query.paginate(page, 10).items
        res = {}
        for product in products:
            if (product.possuiVeiculo == "True"):
                res[product.id] = {
                    'nome': product.nome,
                    'sexo': product.sexo,
                    'tipoVeiculo': product.tipoVeiculo,
                    'veiculoCarregado': product.veiculoCarregado,
                    'idade': product.idade,
                    'cnh': product.cnh,
                    'possuiVeiculo': product.possuiVeiculo,
                    'cepOrigem': product.cepOrigem,
                    'cepDestino': product.cepDestino
                }
        return jsonify(len(res))

    @app.route('/list-type', methods=['GET'])
    def listType(page=1):
        products = User.query.paginate(page, 10).items
        res = {}
        for product in products:
            tipo = 'não preenchido'
            if(product.tipoVeiculo is not None):
                tipo = product.tipoVeiculo

            if (tipo not in res):
                res[tipo] = []

            res[tipo].append({
                'nome': product.nome,
                'sexo': product.sexo,
                'tipoVeiculo': product.tipoVeiculo,
                'veiculoCarregado': product.veiculoCarregado,
                'idade': product.idade,
                'cnh': product.cnh,
                'possuiVeiculo': product.possuiVeiculo,
                'cepOrigem': product.cepOrigem,
                'cepDestino': product.cepDestino
            })
        return jsonify(res)

product_view = ProductView.as_view('product_view')
app.add_url_rule(
    '/users/', view_func=product_view, methods=['GET']
)
app.add_url_rule(
    '/new-user/', view_func=product_view, methods=['POST']
)
app.add_url_rule(
    '/user/<int:id>', view_func=product_view, methods=['GET']
)
app.add_url_rule(
    '/delete-user/<int:id>', view_func=product_view, methods=['DELETE']
)
app.add_url_rule(
    '/edit-user/<int:id>', view_func=product_view, methods=['PUT']
)