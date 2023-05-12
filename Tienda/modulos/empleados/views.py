from flask import Blueprint, render_template, redirect, request
from Tienda.modulos.empleados.model.empleadosOld import EMPLEADOS
from Tienda.modulos.empleados.model.empleados import Empleado
from sqlalchemy import not_, or_
from Tienda.modulos import db

bp_empleados = Blueprint("empleados", __name__)

@bp_empleados.route('/empleados/')
def empleados():
    #for a,b in EMPLEADOS.items():
    #    print(f"{a} : {b}")
    cdx={
        "empleados":Empleado.query.all()
    }
    return render_template("empleados/empleados.html",cdx=cdx)

@bp_empleados.route('/empleados/pruebas')
def pruebas():
    # consulta que solo regresa 2 registros
    Empleado.query.limit(2).all()
    # consulta que regresa los registros ordenados por salario
    Empleado.query.order_by(Empleado.salario.desc()).all()
    #consulta que no regresa una lista, solo 1 empleado
    Empleado.query.get({'id': 2})
    #consulta por nombre, no toma en ceunta las mayusculas
    Empleado.query.filter_by(nombre='Luis').all()
    #consulta los registros menor o igual que jose
    Empleado.query.filter(Empleado.nombre <= 'Jose').all()
    print(Empleado.query.filter_by(nombre='Luis', id=3).all())
    print(Empleado.query.filter(Empleado.nombre.like('%s%')).all())
    print(Empleado.query.filter(not_(Empleado.nombre == 'Jose')).all())
    print(Empleado.query.filter(or_(Empleado.nombre == 'Jose', Empleado.edad > 30)).all())
    # Crear registro
    e = Empleado(nombre='Pedro', apellido='Peralta', sexo='H', edad=32,
                 salario=42160, comentarios='', puesto='patron')
    db.session.add(e)
    db.session.commit()
    # Eliminar registro
    e = Empleado.query.filter_by(nombre='Pedro').first()
    if e:
        db.session.delete(e)
        db.session.commit()
    cdx={
        "empleados":Empleado.query.all()
    }
    return render_template("empleados/empleados.html",cdx=cdx)

@bp_empleados.route('/empleados/comentarios/<int:id>/')
def comentarios(id):
    #empleado = f"id={id}, tipo={type(id)}."
    empleado = Empleado.query.get({'id': id})# EMPLEADOS[id]
    return empleado.comentarios

@bp_empleados.route('/empleados/borrar/<int:id>/', methods=['GET', 'POST'])
def baja(id):
    if request.method == 'GET':
        cdx={
            'tipo':'baja',
            'empleado':Empleado.query.get({'id': id}) #EMPLEADOS[id]
        }
        return render_template("empleados/ABC_empleados.html",cdx=cdx)
    elif request.method == 'POST':
        #del(EMPLEADOS[id])
        e = Empleado.query.get({'id': id})
        if e:
            db.session.delete(e)
            db.session.commit()
        return redirect("/empleados/")
    else:
        return "Error"

@bp_empleados.route('/empleados/cambio/<int:id>/', methods=['GET', 'POST'])
def cambio(id):
    if request.method == 'GET':
        cdx={
            'tipo':'cambio',
            'empleado':Empleado.query.get({'id': id})#EMPLEADOS[id]
        }
        return render_template("empleados/ABC_empleados.html",cdx=cdx)
    elif request.method == 'POST':
        e = Empleado.query.get({'id': id})
        if e:
            e.nombre= request.form.get("nombre")
            e.apellido = request.form.get("apellido")
            sexo = request.form.get("sexo")
            if sexo == '1':
                e.sexo = 'H'
            elif sexo == '2':
                e.sexo = 'M'
            else:
                e.sexo = 'N'
            e.puesto = request.form.get("puesto")
            e.edad = request.form.get("edad")
            salario = request.form.get("salario")
            salario = salario.replace('$','')
            salario = salario.replace(',', '')
            e.salario = float(salario)
            e.comentario = request.form.get("comentario")
            db.session.add(e)
            db.session.commit()


        # EMPLEADOS[id]['nombre'] = request.form.get("nombre")
        # EMPLEADOS[id]['apellido'] = request.form.get("apellido")
        # sexo = request.form.get("sexo")
        # if sexo == '1':
        #     EMPLEADOS[id]['sexo'] = 'H'
        # elif sexo == '2':
        #     EMPLEADOS[id]['sexo'] = 'M'
        # else:
        #     EMPLEADOS[id]['sexo'] = 'N'
        # EMPLEADOS[id]['puesto'] = request.form.get("puesto")
        # salario = request.form.get("salario")
        # salario = salario.replace('$','')
        # salario = salario.replace(',', '')
        # EMPLEADOS[id]['salario'] = float(salario)
        # EMPLEADOS[id]['comentario'] = request.form.get("comentario")


        return redirect("/empleados/")
    else:
        return "Error"

@bp_empleados.route('/empleados/nuevo', methods=['GET', 'POST'])
def alta():
    if request.method == 'GET':
        cdx = {
            'tipo': 'alta',
            'empleado': None
        }
        return render_template("empleados/ABC_empleados.html",cdx=cdx)
    elif request.method == 'POST':
        nombre = request.form.get("nombre")
        apellido = request.form.get("apellido")
        sexo = request.form.get("sexo")
        if sexo == '1':
            sexo = 'H'
        elif sexo == '2':
            sexo = 'M'
        else:
            sexo = 'N'
        puesto = request.form.get("puesto")
        edad = request.form.get("edad")
        salario = request.form.get("salario")
        salario = salario.replace('$', '')
        salario = salario.replace(',', '')
        salario = float(salario)
        comentario = request.form.get("comentario")
        e = Empleado(
            nombre=nombre,
            apellido=apellido,
            sexo=sexo,
            edad=edad,
            puesto=puesto,
            salario=salario,
            comentarios=comentario
        )
        db.session.add(e)
        db.session.commit()
        return redirect("/empleados/")
    else:
        return "ERROR"

@bp_empleados.app_template_filter('formato_moneda')
def formato_moneda(numero:float):
    if(numero):
        return f"${numero:0,.2f}"
    return f"${0:0,.2f}"