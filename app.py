from flask import Flask, request, session, jsonify
from flask_cors import CORS

from api.motoSchema import *

from api.querys import *

app = Flask(__name__)
CORS(app)


@app.route('/login', methods=['POST'])
def login():

    conn = None
    cursor = None
    try:
        _json = request.json
        _username = _json['username']
        _password = _json['password']

        print(_username)
        # validate the received values
        if _username and _password:

            # check user exists
            _query = querys()
            result = _query.get_user_by_username_and_password(
                _username, _password)

            print(result)

            if result:
                session['username'] = result[1]
                return jsonify({'message': 'You are logged in successfully'})

            else:
                resp = jsonify(
                    {'message': 'Bad Request - invalid credendtials'})
                resp.status_code = 400
                return resp

    except Exception as e:
        print(e)

    finally:
        if cursor and conn:
            cursor.close()
            conn.close()


@app.route('/api/v1/info-moto', methods=['GET'])
def info():

    try:

        querys_ = querys()
        results = querys_.get_all()
        data = []
        for result in results:

            data.append({
                "id": result[0],
                "anio": result[4],
                "color": result[5],
                "kilometraje": result[6],
                "marca": result[2],
                "modelo": result[3],
                "precio": result[1],
                "fecha_creacion": result[7]
            })
        return {'message': 'Exitoso', 'data': data}, 200

    except Exception as inst:
        print(inst)
        return {'message': 'Error inesperado'}, 500


@app.route('/api/v1/info-moto/<id>', methods=['DELETE'])
def delete(id):

    try:
        if not id:
            return {'message': 'id requerido'}

        query_ = querys()
        query_.delete(id)

        return {'message': 'Registro eliminado'}, 200

    except Exception as inst:
        print(inst)
        return {'message': 'Error inesperado'}, 500


@app.route('/api/v1/info-moto/<id>', methods=['GET'])
def get_info_by_id(id):
    return id


@app.route('/api/v1/info-moto', methods=['POST'])
def create_info():
    try:

        schema = motoSchema()
        errors = schema.validate(request.json)
        if errors:
            return {'message': 'Validation errors', 'errors': errors}, 400
        query_ = querys()
        query_.insert_(request.json)
        print(request.json)
        return {'message': 'Informacion creada'}, 201

    except Exception as inst:
        print(inst)
        return {'message': 'Error inesperado'}, 500


@app.route('/api/v1/info-moto/<id>', methods=['PUT'])
def update_info(id):

    try:

        schema = motoSchema()
        errors = schema.validate(request.json)
        if errors:
            return {'message': 'Validation errors', 'errors': errors}, 400
        query_ = querys()
        query_.update_record(request.json, id)
        print(request.json)
        return {'message': 'Informacion actualizada'}, 200

    except Exception as inst:
        print(inst)
        return {'message': 'Error inesperado'}, 500

if __name__ == "__main__":
    app.run(debug=True)
