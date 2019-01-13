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

    def get(self, id=None, page=1):
        if not id:
            products = User.query.paginate(page, 10).items
            res = {}
            for product in products:
                res[product.id] = {
                    'nome': product.nome,
                    'sexo': product.sexo,
                    'tipoVeiculo': product.tipoVeiculo,
                }
        else:
            product = User.query.filter_by(id=id).first()
            if not product:
                abort(404)
            res = {
                'name': product.nome,
                'price': product.sexo,
                'tipoVeiculo': product.tipoVeiculo,
            }
        return jsonify(res)

    def post(self):
        nome = request.form.get('nome')
        sexo = request.form.get('sexo')
        tipoVeiculo = request.form.get('tipoVeiculo')
        # veiculoCarregado = request.form.get('veiculoCarregado')
        # idade = request.form.get('idade')
        # cnh = request.form.get('cnh')
        # possuiVeiculo = request.form.get('possuiVeiculo')

        product = User(nome, sexo, tipoVeiculo)
        db.session.add(product)
        db.session.commit()
        return jsonify({product.id: {
            'nome': product.nome,
            'sexo': product.sexo,
            'tipoVeiculo': product.tipoVeiculo,
            # 'veiculoCarregado': product.veiculoCarregado,
            # 'idade': product.idade,
            # 'cnh': product.cnh,
            # 'possuiVeiculo': product.possuiVeiculo,
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
    '/product/', view_func=product_view, methods=['GET', 'POST']
)
app.add_url_rule(
    '/product/<int:id>', view_func=product_view, methods=['GET']
)