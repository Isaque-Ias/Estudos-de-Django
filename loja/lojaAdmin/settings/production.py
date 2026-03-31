from .settings import *

DEBUG = False
#Crie a secret key para seu ambiente de produção
SECRET_KEY = 'Rjqa9(WBUJbjaYP|sUH4<Uh%sSG-Ye5k'
DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
ALLOWED_HOSTS = ['127.0.0.1']