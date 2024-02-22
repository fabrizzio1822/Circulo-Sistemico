<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validar que los campos no estén vacíos
    if (empty($_POST['nombre']) || empty($_POST['telefono']) || empty($_POST['email']) || empty($_POST['mensaje'])) {
        echo "<h2>Error al enviar el formulario</h2>";
        echo "<p>Por favor, completa todos los campos.</p>";
        exit; // Salir del script
    }

    // Sanitizar los datos recibidos
    $nombre = filter_var($_POST['nombre'], FILTER_SANITIZE_STRING);
    $telefono = filter_var($_POST['telefono'], FILTER_SANITIZE_NUMBER_INT);
    $email = filter_var($_POST['email'], FILTER_SANITIZE_EMAIL);
    $mensaje = filter_var($_POST['mensaje'], FILTER_SANITIZE_STRING);

    // Validar el formato del correo electrónico
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo "<h2>Error al enviar el formulario</h2>";
        echo "<p>Por favor, ingresa un correo electrónico válido.</p>";
        exit; // Salir del script
    }

    // Destinatario del correo electrónico 
    $destinatario = "circulosistemico1@gmail.com";

    // Asunto del correo electrónico
    $asunto = "Nuevo formulario de contacto";

    // Mensaje del correo electrónico
    $contenido = "Nombre: $nombre\n";
    $contenido .= "Teléfono: $telefono\n";
    $contenido .= "Correo Electrónico: $email\n";
    $contenido .= "Mensaje: $mensaje\n";

    // Encabezados del correo electrónico
    $headers = "From: $email\r\n";
    $headers .= "Reply-To: $email\r\n";

    // Enviar el correo electrónico
    if (mail($destinatario, $asunto, $contenido, $headers)) {
        // Mostrar un mensaje de éxito si el correo se envió correctamente
        echo "<h2>¡Formulario enviado con éxito!</h2>";
        echo "<p>Gracias por tu contacto. Nos pondremos en contacto contigo pronto.</p>";
    } else {
        // Mostrar un mensaje de error si hay un problema al enviar el correo
        echo "<h2>Error al enviar el formulario</h2>";
        echo "<p>Hubo un problema al procesar tu solicitud. Por favor, inténtalo de nuevo más tarde.</p>";
    }

} else {
    // Si el método de solicitud no es POST, mostrar un mensaje de error
    echo "<h2>Error al enviar el formulario</h2>";
    echo "<p>Se ha producido un error. Por favor, vuelve a intentarlo más tarde.</p>";
}
?>
