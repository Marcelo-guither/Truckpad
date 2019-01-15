from logistica import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    sexo = db.Column(db.String(255))
    tipoVeiculo = db.Column(db.String(255))
    veiculoCarregado = db.Column(db.String(255))
    idade = db.Column(db.String(255))
    cnh = db.Column(db.String(255))
    possuiVeiculo = db.Column(db.String(255))

    def __init__(self, nome, sexo, tipoVeiculo, veiculoCarregado, idade, cnh, possuiVeiculo):
        self.nome = nome
        self.sexo = sexo
        self.tipoVeiculo = tipoVeiculo
        self.veiculoCarregado = veiculoCarregado
        self.idade = idade
        self.cnh = cnh
        self.possuiVeiculo = possuiVeiculo

    def __repr__(self):
        return '<Users %d>' % self.id