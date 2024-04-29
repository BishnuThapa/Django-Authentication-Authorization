from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login,logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            # form.save()
            ## login after register
            auth_login(request, form.save())
            return redirect('/')
    else:
        form=UserCreationForm()

    context={
        'form':form
    }
    return render(request,'user/register.html',context)

def login(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            ## redirects user after login to next url when login required
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            
            return redirect('/')
    else:
        form=AuthenticationForm()
    context = {
        'form': form
    }
    return render(request,'user/login.html',context)

def logout_view(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/users/login/')
def test(request):
    return render(request,'user/test.html')