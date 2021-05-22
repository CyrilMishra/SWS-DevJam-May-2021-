from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import SellForm
from .models import *


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
	id = Signup.objects.get(student_id=request.session['user_id_session_login'])

	total_items = i.count()
	total_user_items = i.filter(student=id).count()

	context = {
		'i_count':total_items , 'ui_count':total_user_items,
	}
	return render(request,'bsi/bsidashboard.html',context)

def sell(request):
	# print(request.POST)

	student_id = Signup.objects.get(student_id=request.session['user_id_session_login'])
	form = SellForm()
	if request.method == 'POST':
		form = SellForm(request.POST)
		c_id = request.POST.get('student')
		c_stu_id = Signup.objects.get(id=c_id)
		print(c_id)
		print(c_stu_id)
		print(student_id)
		if c_stu_id != student_id :
			return HttpResponse("<strong>Please Select You User Id to Post Add.</strong><br><a href='sell'><button>Click Hare To Try again</a>")
		if form.is_valid():
			form.save()
			return redirect('sellpost')
	context= {'form':form}
	return render(request,'bsi/sell.html',context)

def buy(request):
	items = Item.objects.all()
	context={ 'items' : items}
	return render(request,'bsi/alladds.html',context)

def sellpost(request):
	return render(request,'bsi/sellpost.html')

def useradds(request):
	id = Signup.objects.get(student_id=request.session['user_id_session_login'])
	items = Item.objects.filter(student=id)
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

# -------------------(UPDATE VIEWS) -------------------

def updatePost(request):
	myid = request.GET.get('pid')
	print(myid)
	post = Item.objects.get(id=myid)
	form = SellForm(instance=post)

	if request.method == 'GET' and request.GET.get('pid'):
		form = SellForm(request.GET, instance=post)
		if form.is_valid():
			form.save()
			messages.success(request,'Post Updated Successfully')
			return redirect('useradds')
	return redirect('updatePost')


def sellupdate(request,pk):
	post = Item.objects.get(id=pk)
	print(post)
	form = SellForm(instance=post)
	if request.method == 'POST':
		form = SellForm(request.POST, instance=post)
		if form.is_valid():
			form.save()
			return redirect('useradds')
	context = {'form': form}
	return render(request,'bsi/sell.html',context)


# -------------------(DELETE VIEWS) -------------------

def selldelete(request,pk):
	post = Item.objects.get(id=pk)
	if request.method == "POST":
		post.delete()
		return redirect('useradds')
	context ={
		'post':post
	}
	return render(request, 'bsi/delete.html', context)