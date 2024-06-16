from flask import Flask, jsonify, request
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

def calcular_noches(entrada, salida):
    #Dadas dos fechas, una de entrada y otra de salida, calcula cuantos dias durará la estadía.
    fecha_entrada = datetime.strptime(entrada, '%Y-%m-%d')
    fecha_salida = datetime.strptime(salida, '%Y-%m-%d')
    hoy = datetime.today().date()
    if fecha_entrada.date() < hoy:
        return 0
    return (fecha_salida - fecha_entrada).days

app = Flask(__name__)
#Create_engine (de la libreria SQLAlchemy) crea un motor de BDD, el cual administrara conexiones con la misma y ejecutara consultas SQL
engine = create_engine("mysql+mysqlconnector://sql10712305:MP6V7fqkm6@sql10.freemysqlhosting.net:3306/sql10712305")

@app.route('/habitaciones', methods = ['GET'])
def obtener_habitaciones():
    conn = engine.connect() #A traves del motor engine abre una conexion a la BDD y devuelve un objeto 'conn' con el que se pueden ejecutar consultas SQL
    try:
        result = conn.execute(text("SELECT * FROM tipos_habitaciones")) #Selecciona todo de la tabla 'tipos_habitaciones'
    except SQLAlchemyError as err:
        conn.close()    #Cierra la conexion con la BDD
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500
    
    data = []
    for row in result:  #Crea una lista de dicc con la infromacion de las habitaciones
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
    return jsonify(data), 201   #Devuelve en formato json el dicc con la informacion junto al codigo de consulta exitosa


@app.route('/reservar', methods = ['POST'])
def reservar():
    conn = engine.connect()
    reserva = request.get_json()    #Recibe la info del form enviada desde app.py
    
    #Texto con una consulta SQL para encontrar una habitacion disponible del tipo y rango de fecha especificada en el form
    query = text(f"""
            SELECT h.numero FROM habitaciones h
            WHERE h.tipo = '{reserva['tipo']}'
            AND h.numero NOT IN (
                SELECT r.habitacion FROM reservas r
                WHERE '{reserva['entrada']}' < r.salida AND '{reserva['salida']}' > r.entrada
            )
            LIMIT 1
        """)
    
    try:    #Hace la consulta y devuelve si falla el intento 
        result = conn.execute(query)
    except SQLAlchemyError as err:
        conn.close()
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500
    
    habitacion = result.fetchone()  #Fetchone devuelve una fila del resultado como una tupla, si no hay filas devuelve 'None' 
    if habitacion is None:  #Si no habia fila quiere decir que no encontro habitaciones que cumplan las condiciones, devuelve el siguiente mensaje
        return jsonify({'message': f"No hay habitaciones de tipo {reserva['tipo']} disponibles para esas fechas!"}), 404

    try:    #Busca la capacidad maxima de huespedes del tipo de habitacion seleccionada por el usuario
        result = conn.execute(text(f"SELECT capacidad FROM tipos_habitaciones WHERE tipo = '{reserva['tipo']}'"))
    except SQLAlchemyError as err:
        conn.close()
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500
    capacidad = result.fetchone()
    if int(capacidad[0]) < int(reserva["huespedes"]):   #Si la capacidad de la habitacion es menor a la solicitada por el usuario devuelve el siguiente mensaje
        return jsonify({'message': f"En una habitación de tipo {reserva['tipo']} solo entran hasta {capacidad[0]} personas!"}), 404

    try:
        #Busca un descuento correspondiente al código ingresado y verifica su validez (en caso contrario devuelve 0)
        descuento = conn.execute(text(f"""SELECT 
                                      COALESCE(MAX(descuento), 0) AS descuento 
                                      FROM promociones 
                                      WHERE 
                                      codigo = '{reserva['codigo']}' 
                                      AND tipo_habitacion = '{reserva['tipo']}' 
                                      AND NOW() BETWEEN inicio AND fin;"""))
        result = conn.execute(text(f"SELECT precio FROM tipos_habitaciones WHERE tipo = '{reserva['tipo']}'")) #Busca el precio para la habitacion especificada
    except SQLAlchemyError as err:
        conn.close()
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500
    descuento = descuento.fetchone()
    precio = result.fetchone()
    noches = calcular_noches(reserva['entrada'], reserva['salida']) #Llama a funcion aux 'calcular_noches'
    if noches < 1:
        conn.close()
        return jsonify({'message': 'Debe ingresar fechas válidas!'}), 404
    valor_reserva = precio[0] * noches - (precio[0] * noches * descuento[0] * 0.01)  #Multiplica el precio de la habitacion por la cantidad de noches, hace el descuento correspondiente, y obtiene valor total de la reserva
    
    #Modifica la query con un nuevo texto de consulta SQL que va a insertar la nueva reserva en la BDD
    query = text(f"""
            INSERT INTO reservas (usuario, tipo_habitacion, habitacion, entrada, salida, valor, huespedes)
            VALUES ({reserva['usuario']}, '{reserva['tipo']}', {habitacion[0]}, '{reserva['entrada']}', '{reserva['salida']}', '{valor_reserva}', {reserva['huespedes']})""")
    try:    #Intenta insertar los datos de la reserva, devuelve un mensaje si hay alguna excepcion
        conn.execute(query)
        conn.commit()
    except SQLAlchemyError as err:
        conn.close()
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500
    conn.close()
    return jsonify({'message': 'La reserva fue realizada correctamente!'}), 201 #Devuelve un mensaje exitoso en caso de haber llegado a esta linea

@app.route("/mis_reservas", methods = ['GET'])
def obtener_info_reservas():
    conn = engine.connect()
    usuario = request.get_json()    #Recibe la data de la id del usuario en session enviada desde app.py

    try:    #Selecciona todas las reservas del usuario 
        result = conn.execute(text(f"SELECT * FROM reservas WHERE usuario='{usuario['id']}'"))
    except SQLAlchemyError as err:
        conn.close()
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500
    
    data = []
    for row in result:  #Crea una lista de dicc con la infromacion de las reservas del usuario
        entity = {}
        entity['numero'] = row.numero
        entity['usuario'] = row.usuario
        entity['tipo_habitacion'] = row.tipo_habitacion
        entity['habitacion'] = row.habitacion
        entity['entrada'] = row.entrada
        entity['salida'] = row.salida
        entity['valor'] = row.valor
        entity['huespedes'] = row.huespedes
        data.append(entity)
    return jsonify(data), 201

@app.route("/obtener_usuarios", methods = ['GET'])
def obtener_usuarios():
    conn = engine.connect()
    try:
        result = conn.execute(text(f"SELECT * FROM usuarios"))
    except SQLAlchemyError as err:
        conn.close()
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500
    
    data = []
    for row in result:
        entity = {}
        entity['id'] = row.id
        entity['nombre'] = row.nombre
        entity['usuario'] = row.usuario
        entity['email'] = row.email
        data.append(entity)
    return jsonify(data), 201

@app.route('/loguear_usuario', methods = ['GET'])
def loguear_usuario():
    conn = engine.connect()
    usuario = request.get_json()    #Recibe la info del form login enviada desde app.py
    try:
        #Busca en la BDD un email o usuario que coincida con el valor recibido de la casilla Usuario del form login
        result = conn.execute(text(f"SELECT contra FROM usuarios WHERE email='{usuario['user']}' OR usuario='{usuario['user']}';"))
        row = result.fetchone()
        admin = False
        if row is None: #Si no encuentra un email o usuario que coincida, busca en la tabla de administradores
            result = conn.execute(text(f"SELECT contra FROM administradores WHERE email='{usuario['user']}' OR usuario='{usuario['user']}';"))
            row = result.fetchone()
            admin = True
            if row is None: #Si ya paso por la busqueda y no encontró el usuario en la BD, devuelve error usuario incorrecto
                conn.close()
                return jsonify({'message': f"Error, el usuario ingresado es incorrecto!"}), 404
        if row[0] == usuario["contra"]: #Si llego hasta este if significa que econtró un usario, verifica si coincide la contra
            conn.close()
            if not admin:
                return jsonify({'message': f"El usuario '{usuario['user']}' es correcto!"}), 201    #Si coincide manda 201 solicitud exitosa, usuario normal
            else:
                return jsonify({'message': f"El usuario '{usuario['user']}' es correcto y es administrador!"}), 200 #Si coincide manda 200 solicitud exitosa, usuario administrador
        else:   #Si no coincide la contra cae en este else y devuelve error contra incorrecta
            conn.close()
            return jsonify({'message': f"Error, la contrasena es incorrecta!"}), 404
    except SQLAlchemyError as err:
        conn.close()
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500

@app.route('/registrar', methods = ['POST'])
def registrar_usuario():
    conn = engine.connect()
    usuario = request.get_json()    #Recibe la info del form signup enviada desde app.py
    try:    #Intenta seleccionar la id de un presunto usuario con el email ingresado (para ver si ya existe)
        result = conn.execute(text(f"SELECT id FROM usuarios WHERE email='{usuario['email']}';"))
        row = result.fetchone()
        if row is None: #Entra a este if si no existe el email en la BDD
            result = conn.execute(text(f"SELECT id FROM usuarios WHERE usuario='{usuario['user']}';"))  #Ahora consulta por Usuario en vez de email
            row = result.fetchone()
            if row is None: #Entra a este if si tampoco existe el usuario en la BDD
                #Inserta el nuevo usuario y su informacion en la tabla usuarios de la BDD
                result = conn.execute(text(f"""INSERT INTO usuarios (nombre, usuario, email, contra) VALUES 
                                   ('{usuario['nombre']}', '{usuario['user']}', '{usuario['email']}', '{usuario['contra']}');"""))
                conn.commit()
            else:   #Si result.fetchone() no es igual a None, significa que ya existe un usuario con ese Usuario
                conn.close()
                return jsonify({'message': "Error, un usuario ya se encuentra registrado con ese nombre de usuario!"}), 404
        else:   #Si result.fetchone() no es igual a None, significa que ya existe un usuario con ese email
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
    try:    #Busca en la BDD el id del usuario que coinicida con el email logueado
        result = conn.execute(text(f"SELECT id FROM usuarios WHERE email='{usuario['user']}';"))
        row = result.fetchone()
        if row is None: #Si no encuentra por email intenta buscar por usuario y obtener el id
            result = conn.execute(text(f"SELECT id FROM usuarios WHERE usuario='{usuario['user']}';"))
            row = result.fetchone()
    except SQLAlchemyError as err:
        conn.close()
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500
    conn.close()
    return jsonify({'id': row[0]}), 201 #Si no hubo error, devuelve el id del usuario junto al codigo de solicitud exitosa

@app.route('/guardar_opinion', methods=['POST'])
def guardar_opinion():  #NO LA COMENTO PORQUE NO SE SI ESTÁ TERMINADA
    conn = engine.connect()
    try:
        opinion = request.get_json()
        resena = opinion.get('resena')
        rating = int(opinion.get('rating'))
        result = conn.execute(text(f"SELECT nombre FROM usuarios WHERE id='{opinion.get('id')}';"))
        usuario = result.fetchone()

        conn.execute(
            text("INSERT INTO opiniones (usuario, resena, rating) VALUES (:usuario, :resena, :rating)"),
            {"usuario": usuario[0], "resena": resena, "rating": rating}
        )
        conn.commit()
        conn.close()
        return jsonify({"message": "Opinión guardada correctamente."}), 201
    except SQLAlchemyError as err:
        print("Error al ejecutar la consulta SQL:", err)
        return jsonify({'message': 'Se ha producido un error al guardar la opinión.'}), 500
    except Exception as err:
        print("Error al ejecutar la consulta SQL:", err)
        return jsonify({'message': 'Se ha producido un error inesperado.'}), 500

@app.route('/obtener_ultimas_opiniones', methods=['GET'])
def obtener_ultimas_opiniones():    #NO LA COMENTO PORQUE NO SE SI ESTÁ TERMINADA
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT usuario, resena, rating FROM opiniones ORDER BY id_opin DESC LIMIT 5"))
            opiniones = [{'usuario': row[0], 'resena': row[1], 'rating': row[2]} for row in result]
        return jsonify(opiniones), 200
    except SQLAlchemyError as err:
        app.logger.error("Error al ejecutar la consulta SQL: %s", err)
        return jsonify({'message': 'Se ha producido un error en el servidor'}), 500
    
@app.route('/realizar_contacto', methods=['POST'])
def realizar_contacto():
    conn = engine.connect()
    info = request.get_json()   #Recibe la info del form contacto enviada desde app.py
    try:    #Inserta en la BDD la consulta del usuario
        conn.execute(text(f"INSERT INTO contacto (nombre, email, asunto, mensaje) VALUES ('{info['nombre']}', '{info['email']}', '{info['asunto']}', '{info['mensaje']}')"))
        conn.commit()
    except SQLAlchemyError as err:
        conn.close()
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500
    conn.close()
    return jsonify({'message': 'Su consulta fue enviada correctamente!'}), 201

@app.route('/eliminar_reserva/<id>', methods=['DELETE'])
def eliminar_reserva(id):
    conn = engine.connect()
    try:    #Busca la reserva por id y la elimina de la tabla reservas
        conn.execute(text(f"DELETE FROM reservas WHERE numero='{id}';"))
        conn.commit()
    except SQLAlchemyError as err:
        conn.close()
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500
    conn.close()
    return jsonify({'message': "La reserva fue cancelada correctamente!"}), 201

@app.route('/eliminar_usuario/<id>', methods=['DELETE'])
def eliminar_usuario(id):
    conn = engine.connect()
    try:    #Busca la reserva por id y la elimina de la tabla reservas
        conn.execute(text(f"DELETE FROM usuarios WHERE id='{id}';"))
        conn.commit()
    except SQLAlchemyError as err:
        conn.close()
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500
    conn.close()
    return jsonify({'message': "El usuario fue eliminado correctamente!"}), 201

@app.route('/buscar_platos', methods=['GET'])
def buscar_platos():
    conn = engine.connect()  
    try:   
        result = conn.execute(text(f"SELECT * FROM menu;"))
    except SQLAlchemyError as err:
        conn.close()
        return jsonify({'message': 'Se ha producido un error: ' + str(err.__cause__)}), 500
    
    platos = []
    for row in result:  
        entity = {}
        entity['plato'] = row.plato
        entity['descripcion'] = row.descripcion
        entity['precio'] = row.precio
        entity['imagenes'] = row.imagenes
        platos.append(entity)
    return jsonify(platos), 200

if __name__ == "__main__":
    app.run("0.0.0.0", port="5001", debug=True)