from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Pet
from .forms import AdoptionRequestForm, PetForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def view_pets(request):
    species_filter = request.GET.get('species')
    pets = Pet.objects.all()
    if species_filter:
        pets = pets.filter(species__iexact=species_filter)
    return render(request, 'view_pets.html', {'pets': pets})

def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, 'pet_detail.html', {'pet': pet})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def adopt_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)

    if pet.is_adopted:
        return render(request, 'adopt_form.html', {
            'pet': pet,
            'already_adopted': True
        })

    if request.method == "POST":
        form = AdoptionRequestForm(request.POST)
        if form.is_valid():
            adoption = form.save(commit=False)
            adoption.pet = pet
            adoption.user = request.user
            adoption.save()
            return render(request, 'adopt_success.html', {'pet': pet})
    else:
        form = AdoptionRequestForm()

    return render(request, 'adopt_form.html', {'form': form, 'pet': pet})

@login_required
def add_pet(request):
    if request.method == "POST":
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_pets')
    else:
        form = PetForm()
    return render(request, 'add_pet.html', {'form': form})
