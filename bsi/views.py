from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import views
from .models import *
from .forms import SellForm

# Create your views here.
def logout(request):
    try:
        del request.session['user_id_session_login']
    except:
        pass
    else:
        return HttpResponse("<strong>You are logged out.</strong><br><a href='login'>click here to login</a>")

def bsihome(request,):
	i = Item.objects.all()

	total_items = i.count()
	total_user_items = i.filter(student="1").count()

	context = {
		'i_count':total_items , 'ui_count':total_user_items,
	}
	return render(request,'bsi/bsidashboard.html',context)

def sell(request):
	form = SellForm()
	if request.method == 'POST':
		#print('Printing_POST :',request.POST)
		form = SellForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/BSI/sellpost')
	context= {'form':form}
	# context= {'form':form}
	return render(request,'bsi/sell.html',context)

def buy(request):
	items = Item.objects.all()
	context={ 'items' : items}
	return render(request,'bsi/alladds.html',context)

def sellpost(request):
	return render(request,'bsi/sellpost.html')

def useradds(request):
	items = Item.objects.filter(student="1")
	return render(request,'bsi/useradds.html',{'items':items})

def alladds(request):
	if request.GET.get('itemid'):
		ids = request.GET.get('itemid')
		items = Item.objects.filter(id=ids)
		return render(request, 'bsi/alladds.html', {'items': items})
	else:
		items = Item.objects.filter(status="available")
		return render(request, 'bsi/alladds.html', {'items': items})

# Create your views here.
