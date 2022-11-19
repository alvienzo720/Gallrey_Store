from django.shortcuts import render, redirect

from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.views.decorators.csrf import csrf_exempt



def logoutUser(request):
    logout(request)
    return redirect('login')


def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'photolibrary/login.html', {'page': page})


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            if user is not None:
                login(request, user)
                return redirect('home')

    context = {'form': form, 'page': page}
    return render(request, 'photolibrary/register.html', context)


@login_required(login_url='login')
def home(request):
    photos = OurPhoto.objects.all()
    context = {'photos':photos}
    return render(request, 'photolibrary/home.html', context)


def expandImage(request, pk):
    photo = OurPhoto.objects.get(id=pk)
    context = {'photo':photo}
    return render(request, 'photolibrary/expandimage.html', context)


def createPhoto(request):
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data != 'none':
            photo = OurPhoto.objects.create(
                title=data['title'],
                description=data['description'],
                image=image
            )
        return redirect('home')
    return render(request, 'photolibrary/createPhoto.html')



