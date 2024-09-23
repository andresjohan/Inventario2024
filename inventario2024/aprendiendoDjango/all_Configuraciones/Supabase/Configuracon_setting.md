DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_de_tu_base_de_datos',  # El nombre de la base de datos en Supabase
        'USER': 'nombre_de_usuario',           # Usuario que te proporciona Supabase
        'PASSWORD': 'contraseña',              # Contraseña de tu base de datos
        'HOST': 'host.supabase.co',            # Host de tu base de datos (proporcionado por Supabase)
        'PORT': '5432',                        # El puerto es normalmente 5432 para PostgreSQL
    }
}
