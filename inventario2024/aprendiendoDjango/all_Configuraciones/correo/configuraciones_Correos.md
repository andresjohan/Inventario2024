# Creacion Variable entorno (setting)con correo
    `EMAIL_HOST_USER = 'johandrecas@gmail.com'`
     EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'

##        importaciones:
                from email.message import EmailMessage              (Permite Creacion de Mensajes y mesclar con HTML)
                from django.template.loader import render_to_string (permite Mesclarj con plantillas html Mensajes)
                from django.core.mail import send_mail              (allow Envio Correo)
                from django.contrib import messages                 (Mostrar estados de los mensajes)


##   Crear Logica Para envio mensajes vistar normales              
                


