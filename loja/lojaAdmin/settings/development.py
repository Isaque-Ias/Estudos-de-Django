from .settings import *

DEBUG = True
#Crie secret key para seu ambiente de desenvolvimento
SECRET_KEY='cu(&PLYJnpSsOYw)[x*rzJ]R#%$#h;W6'
DATABASES={
    'default':{
        'ENGINE':'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
ALLOWED_HOSTS = ['127.0.0.1']