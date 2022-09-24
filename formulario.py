from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms import StringField, EmailField, SubmitField


class Contactenos(FlaskForm) :
    nombre = StringField('Nombre' , validators=[DataRequired(message='El campo nombre no puede estar vacio'), Length(max=50)])
    correo = EmailField('Correo' , validators=[DataRequired(message='El campo correo es requerido')])
    mensaje = StringField('Mensaje' , validators=[DataRequired(message='El campo mensaje es requerido')])
    enviar = SubmitField('Enviar mensaje')