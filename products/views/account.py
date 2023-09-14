from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

def login_account(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                print("erro: não autenticou")
        
        print("form erro: ", form.errors)
    else:
        form = AuthenticationForm()
    return render(request, 'products/login.html', {'form': form})

def logout_account(request):
    logout(request)
    return redirect('/')
