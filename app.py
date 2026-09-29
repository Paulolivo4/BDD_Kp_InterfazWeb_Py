import os

from flask import Flask, redirect, url_for
from controllers.catequizado_controller import (
    registro_catequizado,
    listar_catequizados,
    editar_catequizado,
    eliminar_catequizado
)

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY') or os.urandom(24).hex()

@app.route('/')
def home():
    return redirect(url_for('listar_catequizados'))

app.add_url_rule('/registro', 'registro_catequizado', registro_catequizado, methods=['GET', 'POST'])
app.add_url_rule('/catequizados', 'listar_catequizados', listar_catequizados)
app.add_url_rule('/catequizado/editar/<id>', 'editar_catequizado', editar_catequizado, methods=['GET', 'POST'])
app.add_url_rule('/catequizado/eliminar/<id>', 'eliminar_catequizado', eliminar_catequizado)

if __name__ == '__main__':
    app.run(debug=True)