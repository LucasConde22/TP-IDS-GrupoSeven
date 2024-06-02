from flask import Flask, jsonify, request
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
engine = create_engine("mysql+mysqlconnector://root@localhost/tp_ids")

@app.route('/loguear_usuario', methods = ['POST'])
def loguear_usuario():
    conn = engine.connect()
    usuario = request.get_json()
    try:
        result = conn.execute(text(f"SELECT contra FROM usuarios WHERE email='{usuario["user"]}';"))
        row = result.fetchone()
        if row is None:
            result = conn.execute(text(f"SELECT contra FROM usuarios WHERE usuario='{usuario["user"]}';"))
            row = result.fetchone()
            if row is None:
                conn.close()
                return jsonify({'message': f"El usuario '{usuario["user"]}' no existe!"}), 404
        if row[0] == usuario["contra"]:
            conn.close()
            return jsonify({'message': f"El usuario '{usuario["user"]}' es correcto!"}), 201
        else:
            conn.close()
            return jsonify({'message': f"La contrasena es incorrecta!"}), 404
    except SQLAlchemyError as err:
        conn.close()
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500

if __name__ == "__main__":
    app.run("127.0.0.1", port="5000", debug=True)