from flask import Flask, jsonify, request
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import datetime

def calcular_noches(entrada, salida): # Falta implementar en función reservar
    return (datetime.strptime(entrada, '%Y-%m-%d') - datetime.strptime(salida, '%Y-%m-%d')).days

app = Flask(__name__)
engine = create_engine("mysql+mysqlconnector://root@localhost/tp_ids")

@app.route('/reservar', methods = ['POST'])
def reservar():
    conn = engine.connect()
    reserva = request.get_json()
    
    query = text(f"""
            SELECT h.numero FROM habitaciones h
            WHERE h.tipo = '{reserva["tipo"]}'
            AND h.numero NOT IN (
                SELECT r.habitacion FROM reservas r
                WHERE '{reserva["entrada"]}' < r.salida AND '{reserva["salida"]}' > r.entrada
            )
            LIMIT 1
        """)
    
    try:
        result = conn.execute(query)
    except SQLAlchemyError as err:
        conn.close()
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500
    
    habitacion = result.fetchone()
    if habitacion is None:
        return jsonify({'message': f"No hay disponibilidad de ese tipo de habitaciones en esa fecha"}), 404

    query = text(f"""
            INSERT INTO reservas (usuario, habitacion, entrada, salida, valor)
            VALUES ({reserva['usuario']}, {habitacion[0]}, '{reserva['entrada']}', '{reserva['salida']}', 
                (SELECT precio FROM tipos_habitaciones WHERE tipo = '{reserva['tipo']}'))""")
    try:
        conn.execute(query)
        conn.commit()
    except SQLAlchemyError as err:
        conn.close()
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500
    conn.close()
    return jsonify({'message': 'La reserva fue realizada!'}), 201

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