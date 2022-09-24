import os
from flask import Flask, render_template
from formulario import Contactenos

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/', methods=['GET','POST'])
def index():
    form = Contactenos()
    return render_template('contacto.html', form=form)