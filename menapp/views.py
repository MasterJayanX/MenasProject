from django.shortcuts import render,redirect
from .models import Login
from .forms import LoginForm







def menu(request):
    return render(request,'menu.html')


def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            return redirect('menu')
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})

