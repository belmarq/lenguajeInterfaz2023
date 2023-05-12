from flask import Blueprint, render_template, redirect, request
from Tienda.modulos.puestos.model.puestos import Puesto
from Tienda.modulos.empleados.model.empleados import Empleado
from sqlalchemy import not_, or_
from Tienda.modulos import db

bp_puestos = Blueprint("puestos", __name__)

@bp_puestos.route('/puestos/')
def puestos():
    cdx={
        "puestos":Puesto.query.all()
    }
    return render_template("puestos/puestos.html",cdx=cdx)

@bp_puestos.route('/puestos/alta/', methods=['GET', 'POST'])
def alta():
    if request.method == 'GET':
        cdx={
            'tipo':'alta',
            'empleados':Empleado.query.all()
        }
        return render_template("puestos/ABC_puestos.html",cdx=cdx)
    elif request.method == 'POST':
        nombre = request.form.get("nombre")
        empleado = int(request.form.get("empleado"))
        empleado = Empleado.query.get({'id': empleado})
        puesto = Puesto(
            puesto=nombre,
            empleado=empleado
        )
        db.session.add(puesto)
        db.session.commit()
        return redirect('/puestos/')


@bp_puestos.route('/puestos/borrar/<int:id>/', methods=['GET', 'POST'])
def baja(id):
    if request.method == 'GET':
        cdx={
            'tipo':'baja',
            'puesto':Puesto.query.get({'id': id}),
            'empleados': Empleado.query.all()
        }
        return render_template("puestos/ABC_puestos.html",cdx=cdx)
    elif request.method == 'POST':
        #del(EMPLEADOS[id])
        e = Puesto.query.get({'id': id})
        if e:
            db.session.delete(e)
            db.session.commit()
        return redirect("/puestos/")
    else:
        return "Error"

@bp_puestos.route('/puestos/cambio/<int:id>/', methods=['GET', 'POST'])
def cambio(id):
    if request.method == 'GET':
        cdx={
            'tipo':'cambio',
             'puesto':Puesto.query.get({'id': id}),
            'empleados': Empleado.query.all()
        }
        return render_template("puestos/ABC_puestos.html",cdx=cdx)
    elif request.method == 'POST':
        nombre = request.form.get("nombre")
        empleado = int(request.form.get("empleado"))
        empleado = Empleado.query.get({'id': empleado})
        e = Puesto.query.get({'id': id})
        if e:
            e.puesto=nombre
            e.empleado=empleado
            db.session.add(e)
            db.session.commit()
        return redirect('/puestos/')