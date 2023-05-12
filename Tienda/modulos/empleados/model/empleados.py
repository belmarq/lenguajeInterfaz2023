from Tienda.modulos import db

class Empleado(db.Model):
    __tablename__="Empleados"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255))
    apellido = db.Column(db.String(255))
    sexo = db.Column(db.String(1))
    edad = db.Column(db.Integer)
    puesto = db.Column(db.String(255))
    salario = db.Column(db.Float)
    comentarios = db.Column(db.String(255))

    def __init__(self, nombre, apellido, sexo, edad, puesto, salario, comentarios=""):
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.edad = edad
        self.puesto = puesto
        self.salario = salario
        self.comentarios = comentarios

    def __repr__(self):
        return f"({self.id}) {self.nombre} {self.apellido}"















