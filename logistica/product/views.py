from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from logistica import db, app
from logistica.product.models import Product

catalog = Blueprint('product', __name__)


@catalog.route('/')
@catalog.route('/home')
def home():
    return "Bem vindo aa API do truckpad"


class ProductView(MethodView):

    def get(self, id=None, page=1):
        if not id:
            products = Product.query.paginate(page, 10).items
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
                }
        else:
            product = Product.query.filter_by(id=id).first()
            if not product:
                abort(404)
            res = {
                'name': product.nome,
                'price': product.sexo,
                'tipoVeiculo': product.tipoVeiculo,
                'veiculoCarregado': product.veiculoCarregado,
                'idade': product.idade,
                'cnh': product.cnh,
                'possuiVeiculo': product.possuiVeiculo,
            }
        return jsonify(res)

    def post(self):
        nome = request.get_json().get('nome')
        sexo = request.get_json().get('sexo')
        tipoVeiculo = request.get_json().get('tipoVeiculo')
        veiculoCarregado = request.get_json().get('veiculoCarregado')
        idade = request.get_json().get('idade')
        cnh = request.get_json().get('cnh')
        possuiVeiculo = request.get_json().get('possuiVeiculo')

        product = Product(nome, sexo, tipoVeiculo, veiculoCarregado, idade, cnh, possuiVeiculo)
        db.session.add(product)
        db.session.commit()
        return jsonify({product.id: {
            'nome': product.nome,
            'sexo': product.sexo,
            'tipoVeiculo': product.tipoVeiculo,
            'veiculoCarregado': product.veiculoCarregado,
            'idade': product.idade,
            'cnh': product.cnh,
            'possuiVeiculo': product.possuiVeiculo,
        }})

    def put(self, id):
        # Update the record for the provided id
        # with the details provided.
        return

    def delete(self, id):
        # Delete the record for the provided id.
        return


product_view = ProductView.as_view('product_view')
app.add_url_rule(
    '/user/', view_func=product_view, methods=['GET', 'POST']
)
app.add_url_rule(
    '/user/<int:id>', view_func=product_view, methods=['GET']
)