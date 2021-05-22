#from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import views
from .models import *
from .forms import *


# Create your views here.

def logout(request):
    try:
        del request.session['user_id_session_login']
    except:
        pass
    else:
        return HttpResponse("<strong>You are logged out.</strong>")

def lfihome(request):
    if not request.session.has_key('user_id_session_login'):
        return redirect('login')
    id = Signup.objects.get(student_id=request.session['user_id_session_login'])
    uli = LostItem.objects.filter(student=id)

    total_lost_items = uli.count()

    ufi = FoundItem.objects.filter(student=id)

    total_found_items = ufi.count()
    context = {
        'uli_count': total_lost_items, 'ufi_count': total_found_items,
    }
    return render(request, 'lfi/lfidashboard.html', context)


def lostreport(request):
    if not request.session.has_key('user_id_session_login'):
        return redirect('login')
    form = LostForm()
    if request.method == 'POST':
        # print('Printing_POST :',request.POST)
        form = LostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('LFI/lostentryadded')
    context = {'form': form}
    return render(request, 'lfi/lostreport.html', context)


def foundreport(request):
    if not request.session.has_key('user_id_session_login'):
        return redirect('login')
    if not request.session.has_key('user_id_session_login'):
        return redirect('login')
    form = FoundForm()
    if request.method == 'POST':
        # print('Printing_POST :',request.POST)
        form = FoundForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('founditemadded')
    context = {'form': form}
    return render(request, 'lfi/foundreport.html', context)


def lostentryadded(request):
    return render(request, 'lfi/lostentryadded.html')


def founditemadded(request):
    return render(request, 'lfi/founditemadded.html')


def matchingitems(request):
    return HttpResponse('match Page work in progress >/ >/ >/')


def userfoundentries(request):
    myid = Signup.objects.get(student_id=request.session['user_id_session_login'])
    if request.GET.get('fid'):
        key = request.GET.get('fid')
        items = FoundItem.objects.filter(id=key)
        return render(request, 'lfi/userfoundentries.html', {'itemsfound': items})
    else:
        items = FoundItem.objects.filter(student=myid.id)
        return render(request, 'lfi/userfoundentries.html', {'items': items})


def userslostentries(request):
    myid = Signup.objects.get(student_id=request.session['user_id_session_login'])
    items = LostItem.objects.filter(student=myid)
    return render(request, 'lfi/userslostentries.html', {'items': items})

# Create your views here.


def lostreportdelete(request,pk):
    report = LostItem.objects.get(id=pk)
    if request.method == "POST":
        report.delete()
        return redirect('userslostentries')
    context = { 'report':report}
    return render(request,'lfi/lostreportdelete.html',context)


def foundreportdelete(request, pk):
    report = FoundItem.objects.get(id=pk)
    if request.method == "POST":
        report.delete()
        return redirect('userfoundentries')
    context = {'report': report}
    return render(request, 'lfi/foundreportdelete.html', context)


def lostreportupdate(request,pk):
    report = LostItem.objects.get(id=pk)
    print(pk)
    form = LostForm(instance = report)
    if request.method == 'POST':
        form = LostForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            return redirect('userslostentries')
    context = {'form': form}
    return render(request, 'lfi/lostreport.html', context)


def foundreportupdate(request,pk):
    report = FoundItem.objects.get(id=pk)
    print(pk)
    # form = FoundForm()
    form = FoundForm(instance = report)
    if request.method == 'POST':
        form = FoundForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            return redirect('userfoundentries')
    context = {'form': form}
    return render(request, 'lfi/foundreport.html', context)