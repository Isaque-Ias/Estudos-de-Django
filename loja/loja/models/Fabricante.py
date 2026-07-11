from loja.models import *
class Fabricante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    perfil = models.IntegerField(choices=PERFIL, default=3)
    Fabricante = models.CharField(null=False, max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.Fabricante)
    
    @receiver
    def create_user_fabricante(sender, instance, created, **kwargs):
        try:
            if created:
                Fabricante.objects.create(user=instance)
        except:
            pass

    @receiver(post_save, sender=User)
    def save_user_fabricante(sender, instance, **kwargs):
        try:
            instance.fabricante.save()
        except:
            pass