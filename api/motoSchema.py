from marshmallow import Schema, fields


class motoSchema(Schema):
    precio = fields.Float(required=True)

    marca = fields.Str(required=True)
    modelo = fields.Str(required=True)
    anio = fields.Integer(required=True)
    color = fields.Str(required=True)
    kilometraje = fields.Str(required=True)
