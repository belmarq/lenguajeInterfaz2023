from Tienda.modulos import db

class Puesto(db.Model):
    __tablename__ = "Puestos"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    puesto = db.Column(db.String(255))
    empleado_id = db.Column(db.Integer, db.ForeignKey("Empleados.id"))
    empleado = db.relationship("Empleado")

    def __init__(self, puesto, empleado):
        self.puesto = puesto
        self.empleado = empleado

    def __repr__(self):
        return f"({self.id}) {self.puesto} {self.empleado.nombre}"