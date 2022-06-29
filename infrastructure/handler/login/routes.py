from flask import request, jsonify
from . import my_blue_user
from model.user import User
from infrastructure.storage.user.userdata import UserData

user_data = UserData()


@my_blue_user.route("/api/v1/login", methods=["POST"])
def login():
    if request.method != 'POST':
        return 'Metodo invalido'

    try:
        user = User(request.json['name'])
        if is_name_empty(user.name):
            return jsonify({'message': "Nombre esta vacio"})

        storage = user_data.add_user(user)
        if not storage:
            return jsonify({'error': "El nombre ingresado ya existe", 'data': user_data.user_data_info()})

        return jsonify({'message': "se creo", 'data': user_data.user_data_info()})

    except Exception as err:
        return jsonify({'error': err})



def is_name_empty(name: str) -> bool:
    return len(name) == 0