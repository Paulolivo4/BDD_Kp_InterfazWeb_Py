from flask import render_template, request, redirect, url_for, flash
from models.catequizado import Catequizado

def registro_catequizado():
    if request.method == 'POST':
        datos = (
            request.form['id'],
            request.form['nombre'],
            request.form['apellido'],
            request.form['fecha_nacimiento'],
            request.form['cedula'],
            request.form['direccion'],
            request.form['telefono'],
            request.form['email'],
            request.form['parroquia_id'],
            request.form['grupo_id']
        )
        try:
            Catequizado.registrar(datos)
            flash('Catequizado registrado correctamente', 'success')
            return redirect(url_for('registro_catequizado'))
        except Exception as e:
            flash(f'Error: {e}', 'danger')
    return render_template('registro_catequizado.html')

def listar_catequizados():
    catequizados = Catequizado.listar()
    return render_template('listar_catequizados.html', catequizados=catequizados)

def editar_catequizado(id):
    catequizado = Catequizado.obtener_por_id(id)
    if not catequizado:
        flash('Catequizado no encontrado', 'danger')
        return redirect(url_for('listar_catequizados'))
    if request.method == 'POST':
        datos = (
            request.form['nombre'],
            request.form['apellido'],
            request.form['fecha_nacimiento'],
            request.form['cedula'],
            request.form['direccion'],
            request.form['telefono'],
            request.form['email'],
            request.form['parroquia_id'],
            request.form['grupo_id'],
            id
        )
        try:
            Catequizado.actualizar(datos)
            flash('Catequizado actualizado correctamente', 'success')
            return redirect(url_for('listar_catequizados'))
        except Exception as e:
            flash(f'Error: {e}', 'danger')
    return render_template('editar_catequizado.html', catequizado=catequizado)

def eliminar_catequizado(id):
    try:
        Catequizado.eliminar(id)
        flash('Catequizado eliminado correctamente', 'success')
    except Exception as e:
        flash(f'Error: {e}', 'danger')
    return redirect(url_for('listar_catequizados'))