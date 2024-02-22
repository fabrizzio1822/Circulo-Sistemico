from flask import Flask, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/enviar_formulario', methods=['POST'])
def enviar_formulario():
    if request.method == 'POST':
        # Validar que los campos no estén vacíos
        if not all(field in request.form for field in ['nombre', 'telefono', 'email']):
            return "<h2>Error al enviar el formulario</h2><p>Por favor, completa todos los campos.</p>"

        # Sanitizar los datos recibidos
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        email = request.form['email']

        # Validar el formato del correo electrónico
        if '@' not in email:
            return "<h2>Error al enviar el formulario</h2><p>Por favor, ingresa un correo electrónico válido.</p>"

        destinatario = "circulosistemico1@gmail.com"

        # Asunto del correo electrónico
        asunto = "Nuevo formulario de contacto"

        # Cuerpo del correo electrónico
        mensaje = f"Nombre: {nombre}\nTeléfono: {telefono}\nCorreo Electrónico: {email}"

        # Configurar el servidor SMTP
        smtp_server = 'smtp.gmail.com'
        port = 587
        sender_email = 'tucorreodeejemplo@gmail.com'  # Cambia esto por tu dirección de correo
        password = 'tupassword'  # Cambia esto por tu contraseña

        # Crear el objeto MIMEText
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = destinatario
        msg['Subject'] = asunto
        msg.attach(MIMEText(mensaje, 'plain'))

        # Iniciar sesión en el servidor SMTP
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, password)

        # Enviar el correo electrónico
        server.sendmail(sender_email, destinatario, msg.as_string())
        server.quit()

        # Mostrar un mensaje de éxito si el correo se envió correctamente
        return "<h2>¡Formulario enviado con éxito!</h2><p>Gracias por tu contacto. Nos pondremos en contacto contigo pronto.</p>"
    else:
        # Si el método de solicitud no es POST, mostrar un mensaje de error
        return "<h2>Error al enviar el formulario</h2><p>Se ha producido un error. Por favor, vuelve a intentarlo más tarde.</p>"

if __name__ == '__main__':
    app.run(debug=True)
