# Truckpad

Python version `3.7.2`

Frameworks utilizados `Instalação do flask` e `Instalação do sqlalchemy`;


Requisições via POSTMAN

    'http://localhost:5000/users/'                  ['GET']
    Explicação: Traz todos os usuarios cadastrados no banco de dados
    
    'http://localhost:5000/new-user/'               ['POST']
    Explicação: Salva usuários no banco
    HEADER = 
        KEY:    Content-Type
        VALUE:  application/json
    body=
        {
            "nome": "Marcelo",
            "sexo": "Masculino",
            "tipoVeiculo": "Bike",
            "veiculoCarregado": "True",
            "idade": "17",
            "cnh": "NT",
            "possuiVeiculo": "True",
            "cepOrigem": "02856050",
            "cepDestino": "01227200"
        }
    
    'http://localhost:5000/user/<int:id>'           ['GET']
    Explicação: Retorna usuario requerido ao passar o id do mesmo
    
    'http://localhost:5000/delete-user/<int:id>'    ['DELETE']
    Explicação: Remove usuario ao passar o id do mesmo
    
    'http://localhost:5000/edit-user/<int:id>'      ['PUT']
    Explicação: Edita informação do usuario ao passar o ID do mesmo e a informação
    que deve ser editada
    HEADER = 
        KEY:    Content-Type
        VALUE:  application/json
    body=
        {
            "nome": "Araujo",
        }
    
    'http://localhost:5000/list-type'               ['GET']
    Explicação: Lista entregas para cada tipo de veiculo
    
    'http://localhost:5000/own-vehicle'             ['GET']
    Explicação: Retorna quantidade de veiculos com automovel próprio
    
    'http://localhost:5000/user-noload'             ['GET']
    Explicação: Retorna usuarios sem carga

Como rodar a aplicação

    Entrar na pasta do projeto 'Truckpad'
    rodar o app para subir a aplicação 'python app.py'