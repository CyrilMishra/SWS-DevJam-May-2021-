#from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import views
from .models import *
from .forms import *


# Create your views here.

def lfihome(request):
    li = LostItem.objects.all()

    total_lost_items = li.count()

    fi = FoundItem.objects.all()

    total_found_items = fi.count()
    context = {
        'uli_count': total_lost_items, 'ufi_count': total_found_items,
    }
    return render(request, 'lfi/lfidashboard.html', context)


def lostreport(request):
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
    form = FoundForm()
    if request.method == 'POST':
        # print('Printing_POST :',request.POST)
        form = FoundForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('LFI/founditemadded')
    context = {'form': form}
    return render(request, 'lfi/foundreport.html', context)


def lostentryadded(request):
    return render(request, 'lfi/lostentryadded.html')


def founditemadded(request):
    return render(request, 'lfi/founditemadded.html')


def matchingitems(request):
    return HttpResponse('match Page work in progress >/ >/ >/')


def userfoundentries(request):
    items = FoundItem.objects.filter(student="1")
    return render(request, 'lfi/userfoundentries.html', {'items': items})


def userslostentries(request):
    items = LostItem.objects.filter(student="2")
    return render(request, 'lfi/userslostentries.html', {'items': items})

# Create your views here.
