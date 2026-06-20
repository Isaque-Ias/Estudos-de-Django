from django.urls import path
from loja.views.HomeView import home_view
from loja.views.ProdutoView import list_produto_view

urlpatterns = [
    path("", home_view, name= 'home'),
    path("<int:id>", list_produto_view, name= 'produto'),
]