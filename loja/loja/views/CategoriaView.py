from loja.models import Produto
from datetime import timedelta
from django.utils import timezone
from django.shortcuts import render, redirect
from loja.models import Categoria
from django.core.files.storage import FileSystemStorage

def edit_categoria_postback(request, id=None):
    if request.method == 'POST':
        print(request.POST)
        id = request.POST.get("id")
        categoria = request.POST.get("Categoria")
        
        print("postback")
        print(id)
        print(categoria)
        try:
            obj_categoria = Categoria.objects.filter(id=id).first()
            obj_categoria.Categoria = categoria
            obj_categoria.save()
            print("Categoria %s salva com sucesso" % categoria)
        except Exception as e:
            print("Erro salvando edição de categoria: %s" % e)
    return redirect("/categoria")

def list_categoria_view(request, id=None):
    categoria = request.GET.get("categoria")
    
    dias = request.GET.get("dias")
    categorias = Categoria.objects.all()

    if dias is not None:
        now = timezone.now()
        now = now - timedelta(days = int(dias))
        categorias = categorias.filter(criado_em__gte=now)
    if categoria is not None:
        categorias = categorias.filter(Categoria=categoria)

    if id is not None:
        categorias = categorias.filter(id=id)
    print(categorias)
    context = {'categorias': categorias}
    return render(request, template_name='categoria/categoria.html', context=context, status=200)

def edit_categoria_view(request, id=None):
    categorias = Categoria.objects.all()
    if id is not None:
        categorias = categorias.filter(id=id)
    categoria = categorias.first()
    print(categoria)
    # Fabricantes = Fabricante.objects.all()
    # Categorias = Categoria.objects.all()
    context = {'categoria': categoria}#{ 'produto': produto, 'fabricantes' : Fabricantes, 'categorias' : Categorias }
    return render(request, template_name='categoria/categoria-edit.html', context=context, status=200)

def details_categoria_view(request, id=None):
    # Processa o evento GET gerado pela action
    categorias = Categoria.objects.all()
    if id is not None:
        categorias = categorias.filter(id=id)
    categoria = categorias.first()
    print(categoria)
    # fabricantes = Fabricante.objects.all()
    # categorias = Categoria.objects.all()
    context = {'categoria': categoria}#{'produto': produto, 'fabricantes' : fabricantes, 'categorias' : categorias}
    return render(request, template_name='categoria/categoria-details.html', context=context, status=200)

def delete_categoria_view(request, id=None):
    # Processa o evento GET gerado pela action
    categorias = Categoria.objects.all()
    if id is not None:
        categorias = categorias.filter(id=id)
    categoria = categorias.first()
    print(categoria)
    # Fabricantes = Fabricante.objects.all()
    # Categorias = Categoria.objects.all()
    context = {'categoria': categoria}#{'produto': produto, 'fabricantes' : Fabricantes, 'categorias' : Categorias}
    return render(request, template_name='categoria/categoria-delete.html', context=context, status=200)

def delete_categoria_postback(request, id=None):
    if request.method == 'POST':
        id = request.POST.get("id")
        categoria = request.POST.get("Categoria")
        print("postback-delete")
        print(id)
        try:
            categoria_obj = Categoria.objects.filter(id=id)
            categoria_obj.delete()
            print("Categoria %s excluido com sucesso" % categoria)
        except Exception as e:
            print("Erro ao excluir categoria: %s" % e)
    return redirect("/categoria")

def create_categoria_view(request, id=None):
    # Processa o post back gerado pela action
    if request.method == 'POST':
        categoria = request.POST.get("Categoria")
        print("postback-create")
        print(categoria)
        try:
            obj_categoria = Categoria()
            obj_categoria.Categoria = categoria
            obj_categoria.criado_em = timezone.now()
            obj_categoria.alterado_em = obj_categoria.criado_em
            obj_categoria.save()
            print("Categoria %s salvo com sucesso" % categoria)
        except Exception as e:
            print("Erro inserindo categoria: %s" % e)
        return redirect("/categoria")

    # Fabricantes = Fabricante.objects.all()
    # Categorias = Categoria.objects.all()
    context = {}#{'fabricantes' : Fabricantes, 'categorias' : Categorias}
    return render(request, template_name='categoria/categoria-create.html', context=context, status=200)