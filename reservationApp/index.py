from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Q 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# deconnection
def LOGOUT(request):
    logout(request)
    return redirect('connection')

# connexion à la plateforme
def SINGIN(request):
    if request.method == "POST":
        email = request.POST.get('username', None)
        password = request.POST.get('password', None)

        user = User.objects.filter(username=email).first()
        if user:
            auth_user = authenticate(username=user.username, password=password)
            if auth_user:
                login(request, auth_user)
                return redirect('dashbord')
            else:
                print("Mot de passe incorrect")
        else:
            print("L'utilisateur n'existe pas")
        # print("=="*5, " NEW POST:",name,password, "=="*5 )
    return render(request, 'connection.html')

def recuperation(request):
    return render(request,'recuperation.html')

@login_required(login_url='login')
def dashbord(request):
    return render(request, 'dashbord.html')

def connection(request):
    return render(request,'connection.html')

def code(request):
    return render(request,'code_recuperation.html')

@login_required(login_url='login')
def Reservation(request):
    return render(request,'reservation.html')

@login_required(login_url='login')
def Service(request):
    return render(request,'service.html')

def REGISTER(request):
    error = False
    message = ""
    if request.method == "POST":
        name = request.POST.get('nom', None)
        email = request.POST.get('email', None)
        contact = request.POST.get('contact', None)
        password = request.POST.get('password', None)
        passwordOubl = request.POST.get('passwordOubl', None)

        if error == False:
            if password!=passwordOubl:
                error=True
                message="Les mots de passe de correspondent pas!"
        # exit
        user = User.objects.filter(Q(username=name) | Q(password=password)).first()
        if user:
            error=True
            message = f"Un utilisateur avec le pseudo {name}, {email}, {contact} ou le mot de passe {password} existe déjà!"
        # register
        if error == False:
            user = User(
                username = name,
                email = email,
                first_name = contact,
            )
            user.save()
            user.password = password
            user.set_password(user.password)
            user.save()
            return redirect('connection')    
    context = {
        'error':error,
        'message':message
    }
    return render(request,'register.html', context)

@login_required(login_url='login')
def Residence(request):
    return render(request,'residence.html')

@login_required(login_url='login')
def Gestion(request):
    return render(request,'gestion.html')

@login_required(login_url='login')
def Client(request):
    return render(request,'client.html')

def Recuperation(request):
    return render(request,'recuperation.html')