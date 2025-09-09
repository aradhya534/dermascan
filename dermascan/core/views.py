from rest_framework import viewsets
from .models import User, Scan, ChatMessage
from .serializers import UserSerializer, ScanSerializer, ChatMessageSerializer
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required


User = get_user_model()

class CustomLoginView(LoginView):
    template_name = "index.html"
@login_required
def home(request):
    return render(request, 'home.html', {'username': request.user.username, 'name': request.user.name})

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully!")
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})


@login_required
def scan(request):
    return render(request, 'scan.html')

@login_required
def articles(request):
    return render(request, 'articles.html')

@login_required
def chat(request):
    return render(request, 'chat.html')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ScanViewSet(viewsets.ModelViewSet):
    queryset = Scan.objects.all()
    serializer_class = ScanSerializer


class ChatMessageViewSet(viewsets.ModelViewSet):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer
