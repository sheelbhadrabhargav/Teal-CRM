from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Userprofile
from team.models import Team

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            Userprofile.objects.create(user=user)
            
            team=Team.objects.create(user=user)
            team.members.add(request.user)
            team.save()
            
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'userprofile/signup.html', {'form':form})

#def login(request):   Don't know why it is here but I am not touching it until my project is compelete.
#    return render(request, 'userprofile/login.html')

@login_required
def myaccount(request):
    team = Team.objects.filter(created_by=request.user)[0]
    return render(request, 'userprofile/myaccount.html', {
        'team':team})