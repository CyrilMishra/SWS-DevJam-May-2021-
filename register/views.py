from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *

from .forms import SignupForm


# Create your views here.
def logout(request):
    try:
        del request.session['user_id_session_login']
    except:
        pass
    else:
        return HttpResponse("<strong>You are logged out.</strong><a href='login'>click here to login</a>")


def home(request):

    return render(request, 'accounts/dashboard.html')


def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        # print('Printing_POST :',request.POST)
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    context = {'form': form}

    return render(request, 'accounts/signup_form.html', context)


def update_profile(request, pk):
    form = SignupForm()
    context = {}
    return render(request, 'accounts/signup_form.html', context)


def login(request):
    if request.session.has_key('user_id_session_login'):
        user_id = request.session['user_id_session_login']
        context = {
            "user": user_id
        }
        return render(request, 'accounts/dashboard.html', context)
    if request.method == "POST" and request.POST.get('submit'):
        print('Printing_POST :', request.POST)
        user_id = request.POST.get('userid')
        user_pass = str(request.POST.get('password'))
        try:
            data = Signup.objects.get(student_id=user_id)
        except:
            print("user not found")
        else:
            datapass = str(Signup.objects.get(student_id=user_id).password)
            if datapass == user_pass:
                #creating session here
                request.session['user_id_session_login'] = user_id
                print("login success")
                context = {
                    "user" : user_id
                }
                return render(request,'accounts/dashboard.html',context)
                #return redirect('home')

            else:
                print("password is in correct")
                return render(request, 'accounts/login.html')
    return render(request, 'accounts/login.html')

        #print(data)

    #return render(request, 'accounts/login.html',)


def user_registration(request):
    return render(request, 'accounts/user_registration.html')
