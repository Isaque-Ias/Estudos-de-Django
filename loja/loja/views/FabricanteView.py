from loja.models import Fabricante
from django.shortcuts import render, redirect, get_object_or_404
from loja.forms.UserFabricanteForm import UserFabricanteForm, UserForm

def list_fabricante_view(request, id=None):
    # carrega somente usuarios, não inclui os admin
    fabricantes = Fabricante.objects.filter(perfil=3)
    context = {
    'fabricantes': fabricantes
    }
    return render(request, template_name='fabricante/fabricante.html', context=context, status=200)
    
def edit_fabricante_view(request):
    fabricante = Fabricante.objects.filter(user=request.user).first()
    emailUnused = True
    message = None
    if request.method == 'POST':
        fabricanteForm = UserFabricanteForm(request.POST, instance=fabricante, current_user=request.user)
        userForm = UserForm(request.POST, instance=request.user)
        verifyEmail = Fabricante.objects.filter(user__email=request.POST['email']).exclude(user__id=request.user.id).first()
        emailUnused = verifyEmail is None
    else:
        fabricanteForm = UserFabricanteForm(instance=fabricante, current_user=request.user)
        userForm = UserForm(instance=request.user)
    if fabricanteForm.is_valid() and userForm.is_valid() and emailUnused:
        fabricanteForm.save()
        userForm.save()
        message = { 'type': 'success', 'text': 'Dados atualizados com sucesso' }
    else:
        if request.method == 'POST':
            if emailUnused:
                message = { 'type': 'danger', 'text': 'Dados inválidos' }
            else:
                message = { 'type': 'warning', 'text': 'E-mail já usado' }
    context = {
        'fabricanteForm': fabricanteForm,
        'userForm': userForm,
        'message': message
    }
    return render(request, template_name='fabricante/fabricante-edit.html', context=context, status=200)