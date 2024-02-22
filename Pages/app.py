from flask import Flask, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/enviar_formulario', methods=['POST'])
def enviar_formulario():
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        email = request.form['email']
        mensaje = request.form['mensaje']

        # Configurar el correo electrónico
        destinatario = "circulosistemico1@gmail.com"
        asunto = "Nuevo mensaje de contacto"
        cuerpo_mensaje = f"Nombre: {nombre}\nTeléfono: {telefono}\nCorreo Electrónico: {email}\nMensaje: {mensaje}"

        # Configurar el servidor SMTP
        smtp_server = 'smtp.gmail.com'
        port = 587
        sender_email = 'fabrizzioparrillistrabajo@gmail.com'  # Cambia esto por tu dirección de correo
        password = 'acef1822'  # Cambia esto por tu contraseña

        # Crear el objeto MIMEText
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = destinatario
        msg['Subject'] = asunto
        msg.attach(MIMEText(cuerpo_mensaje, 'plain'))

        # Iniciar sesión en el servidor SMTP
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, password)

        # Enviar el correo electrónico
        server.sendmail(sender_email, destinatario, msg.as_string())
        server.quit()

        # Mostrar un mensaje de éxito si el correo se envió correctamente
        return "<h2>¡Formulario enviado con éxito!</h2><p>Gracias por tu mensaje. Nos pondremos en contacto contigo pronto.</p>"
    else:
        # Si el método de solicitud no es POST, mostrar un mensaje de error
        return "<h2>Error al enviar el formulario</h2><p>Se ha producido un error. Por favor, vuelve a intentarlo más tarde.</p>"

if __name__ == '__main__':
    app.run(debug=True)