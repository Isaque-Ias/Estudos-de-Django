from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .Categoria import Categoria
PERFIL = (
(1, 'Admin'),
(2, 'Usuario'),
(3, 'Fabricante'),
)
from .Fabricante import Fabricante
from .Produto import Produto
from .Usuario import Usuario