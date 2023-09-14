from django.urls import path
from products.views.product import list_products, create_product, update_product, delete_product
from products.views.account import login_account, logout_account

urlpatterns = [
    path('', list_products, name='index'),
    path('produto/cadastrar', create_product, name="cadastrar-produto"),
    path('produto/atualizar/<int:id>', update_product, name="atualizar-produto"),
    path('produto/deletar/<int:id>', delete_product, name="deletar-produto"),
    path('login/', login_account, name='login'),
    path('logout/', logout_account, name='logout'),

]
