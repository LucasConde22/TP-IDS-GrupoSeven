from flask import Flask, jsonify, request
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

def calcular_noches(entrada, salida):
    """
    Dadas dos fechas, una de entrada y otra de salida, calcula cuantos
    dias durará la estadía.
    """ 
    return (datetime.strptime(salida, '%Y-%m-%d') - datetime.strptime(entrada, '%Y-%m-%d')).days

app = Flask(__name__)
engine = create_engine("mysql+mysqlconnector://sql10712305:MP6V7fqkm6@sql10.freemysqlhosting.net:3306/sql10712305")

@app.route('/habitaciones', methods = ['GET'])
def obtener_habitaciones():
    conn = engine.connect()
    try:
        result = conn.execute(text("SELECT * FROM tipos_habitaciones"))
    except SQLAlchemyError as err:
        conn.close()
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500
    
    data = []
    for row in result:
        entity = {}
        entity['tipo'] = row.tipo
        entity['caracteristicas'] = row.caracteristicas
        entity['capacidad'] = row.capacidad
        entity['precio'] = row.precio
        entity['foto1'] = row.foto1
        entity['foto2'] = row.foto2
        entity['foto3'] = row.foto3
        entity['video'] = row.video

        data.append(entity)
    return jsonify(data), 201


@app.route('/reservar', methods = ['POST'])
def reservar():
    conn = engine.connect()
    reserva = request.get_json()
    
    query = text(f"""
            SELECT h.numero FROM habitaciones h
            WHERE h.tipo = '{reserva['tipo']}'
            AND h.numero NOT IN (
                SELECT r.habitacion FROM reservas r
                WHERE '{reserva['entrada']}' < r.salida AND '{reserva['salida']}' > r.entrada
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
        return jsonify({'message': f"No hay habitaciones de tipo {reserva['tipo']} disponibles para esas fechas!"}), 404

    try:
        result = conn.execute(text(f"SELECT capacidad FROM tipos_habitaciones WHERE tipo = '{reserva['tipo']}'"))
    except SQLAlchemyError as err:
        conn.close()
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500
    capacidad = result.fetchone()
    if int(capacidad[0]) < int(reserva["huespedes"]):
        return jsonify({'message': f"En una habitación de tipo {reserva['tipo']} solo entran hasta {capacidad[0]} personas!"}), 404

    try:
        result = conn.execute(text(f"SELECT precio FROM tipos_habitaciones WHERE tipo = '{reserva['tipo']}'"))
    except SQLAlchemyError as err:
        conn.close()
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500
    precio = result.fetchone()
    noches = calcular_noches(reserva['entrada'], reserva['salida'])
    valor_reserva = precio[0] * noches

    query = text(f"""
            INSERT INTO reservas (usuario, tipo_habitacion, habitacion, entrada, salida, valor, huespedes)
            VALUES ({reserva['usuario']}, '{reserva['tipo']}', {habitacion[0]}, '{reserva['entrada']}', '{reserva['salida']}', '{valor_reserva}', {reserva['huespedes']})""")
    try:
        conn.execute(query)
        conn.commit()
    except SQLAlchemyError as err:
        conn.close()
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500
    conn.close()
    return jsonify({'message': 'La reserva fue realizada correctamente!'}), 201

@app.route("/mis_reservas", methods = ['GET'])
def obtener_info_reservas():
    conn = engine.connect()
    usuario = request.get_json()

    try:
        result = conn.execute(text(f"""SELECT numero, tipo_habitacion, habitacion, entrada, salida, valor, huespedes
                                   FROM reservas WHERE usuario='{usuario['id']}'"""))
    except SQLAlchemyError as err:
        conn.close()
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500
    
    data = []
    for row in result:
        entity = {}
        entity['numero'] = row.numero
        entity['tipo_habitacion'] = row.tipo_habitacion
        entity['habitacion'] = row.habitacion
        entity['entrada'] = row.entrada
        entity['salida'] = row.salida
        entity['valor'] = row.valor
        entity['huespedes'] = row.huespedes
        data.append(entity)
    return jsonify(data), 201

@app.route('/loguear_usuario', methods = ['POST'])
def loguear_usuario():
    conn = engine.connect()
    usuario = request.get_json()
    try:
        result = conn.execute(text(f"SELECT contra FROM usuarios WHERE email='{usuario['user']}';"))
        row = result.fetchone()
        if row is None:
            result = conn.execute(text(f"SELECT contra FROM usuarios WHERE usuario='{usuario['user']}';"))
            row = result.fetchone()
            if row is None:
                conn.close()
                return jsonify({'message': f"Error, el usuario ingresado es incorrecto!"}), 404
        if row[0] == usuario["contra"]:
            conn.close()
            return jsonify({'message': f"El usuario '{usuario['user']}' es correcto!"}), 201
        else:
            conn.close()
            return jsonify({'message': f"Error, la contrasena es incorrecta!"}), 404
    except SQLAlchemyError as err:
        conn.close()
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500

@app.route('/registrar', methods = ['POST'])
def registrar_usuario():
    conn = engine.connect()
    usuario = request.get_json()
    try:
        result = conn.execute(text(f"SELECT id FROM usuarios WHERE email='{usuario['email']}';"))
        row = result.fetchone()
        if row is None:
            result = conn.execute(text(f"SELECT id FROM usuarios WHERE usuario='{usuario['user']}';"))
            row = result.fetchone()
            if row is None:
                result = conn.execute(text(f"""INSERT INTO usuarios (nombre, usuario, email, contra) VALUES 
                                   ('{usuario['nombre']}', '{usuario['user']}', '{usuario['email']}', '{usuario['contra']}');"""))
                conn.commit()
            else:
                conn.close()
                return jsonify({'message': "Error, un usuario ya se encuentra registrado con ese nombre de usuario!"}), 404
        else:
            conn.close()
            return jsonify({'message': "Error, un usuario ya se encuentra registrado con ese correo electrónico!"}), 404
    except SQLAlchemyError as err:
        conn.close()
        return jsonify({'message': 'Se ha producido un error'}), 500
    conn.close()
    return jsonify({'message': "Usuario creado correctamente!"}), 201

@app.route('/id', methods = ['GET'])
def obtener_id():
    conn = engine.connect()
    usuario = request.get_json()
    try:
        result = conn.execute(text(f"SELECT id FROM usuarios WHERE email='{usuario['user']}';"))
        row = result.fetchone()
        if row is None:
            result = conn.execute(text(f"SELECT id FROM usuarios WHERE usuario='{usuario['user']}';"))
            row = result.fetchone()
    except SQLAlchemyError as err:
        conn.close()
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500
    conn.close()
    return jsonify({'id': row[0]}), 201

if __name__ == "__main__":
    app.run("127.0.0.1", port="5000", debug=True)