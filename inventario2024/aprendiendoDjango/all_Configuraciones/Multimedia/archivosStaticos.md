# Estaticos

# crear carpeta static  para css y html
 
#      Agregar a Ruta Global   en Settings 
            ``STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)       ``

            `cargar a las plantillas de html / crear etiqueta link`                           |   
                `{% load static %}`
                ` <link rel="stylesheet"  href="{% static 'styles.css' %}">`
    
# Templates  (agregar a los settings en las rutas)

    `'DIRS': [os.path.join('templates')],`

