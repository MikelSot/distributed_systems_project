from flask import Flask, jsonify
from flask_socketio import SocketIO, emit
from infrastructure.handler.login import my_blue_user


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/comer',  methods=['GET'])
def ping():
    return jsonify({"gaaaa":"ashbcjs bb   hba"})

app.register_blueprint(my_blue_user)


if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=10000, debug=True)


