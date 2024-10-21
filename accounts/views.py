from django.shortcuts import render, redirect
from .models import User
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from inventaire.models import Objet

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Ne pas encore sauvegarder l'utilisateur
            # Le champ user_compte_id sera généré automatiquement
            user.save()  # Sauvegarde de l'utilisateur avec la logique définie dans models.py
            messages.success(request, "Inscription réussie ! Vous pouvez vous connecter.")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['user_login']
            password = form.cleaned_data['user_password']
            try:
                user = User.objects.get(user_login=login, user_password=password)

                # Si l'utilisateur est trouvé, il est connecté
                messages.success(request, f"Bienvenue {user.user_login}")
                return redirect('home')  # Redirige vers la page d'accueil ou tableau de bord
            except User.DoesNotExist:
                messages.error(request, "Mauvais login ou mot de passe")
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def home_view(request):
    objets = Objet.objects.all()
    return render(request, 'inventaire/objet_list.html', {'objets': objets})