from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request, 'chatApp/index.html')

def room(request, room_name):
    return render(request, 'chatApp/chatroom.html', {
        'room_name': room_name
    })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'chatApp/signup.html', {'form': form})