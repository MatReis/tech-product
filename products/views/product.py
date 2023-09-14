from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from products.models import Product
from products.forms import ProductForm

@login_required
def list_products(request):
    print('request: ',request.user.is_authenticated , "\n\n")
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products} )

@login_required
def create_product(request):
    if request.method == "POST":  
        form = ProductForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/')  
            except:  
                pass  
    else:  
        form = ProductForm()
    
    return render(request, 'products/product_form.html', {'product_action': "Cadastrar"})

@login_required
def update_product(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('index')  
            except Exception as e: 
                print("Erro: ", str(e))
        else: 
            print("form não é valido: ", form.errors)    

    return render(request, 'products/product_form.html', {'product_action': "Atualizar", 'product': product})

def delete_product(request, id):
    product = Product.objects.get(id=id)
    try:
        product.delete()
    except:
        pass
    return redirect('/')
