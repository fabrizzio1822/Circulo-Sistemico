from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuración del servidor de correo
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'tucorreodeejemplo@gmail.com'
app.config['MAIL_PASSWORD'] = 'tupassword'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/')
def formulario():
    return render_template('formulario.html')

@app.route('/enviar_formulario', methods=['POST'])
def enviar_formulario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        email = request.form['email']

        message = Message('Nuevo formulario de contacto',
                          sender='tucorreodeejemplo@gmail.com',
                          recipients=['circulosistemico1@gmail.com'])
        message.body = f"Nombre: {nombre}\nTeléfono: {telefono}\nCorreo Electrónico: {email}"

        mail.send(message)

        return "<h2>¡Formulario enviado con éxito!</h2><p>Gracias por tu contacto. Nos pondremos en contacto contigo pronto.</p>"

if __name__ == '__main__':
    app.run(debug=True)
