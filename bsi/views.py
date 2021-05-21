from django.contrib import messages
from django.http import HttpResponse
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
	if not request.session.has_key('user_id_session_login'):
		return redirect('login')
	i = Item.objects.all()
	id = Signup.objects.get(student_id=request.session['user_id_session_login'])

	total_items = i.count()
	total_user_items = i.filter(student=id).count()

	context = {
		'i_count':total_items , 'ui_count':total_user_items,
	}
	return render(request,'bsi/bsidashboard.html',context)

def sell(request):
	if not request.session.has_key('user_id_session_login'):
		return redirect('login')
	if request.method == 'POST' and request.POST.get('update')  :
		myid = request.GET.get('kid')
		print(myid)
		post = Item.objects.get(id=myid)
		form = SellForm(instance=post)
		if request.method == 'GET' and request.GET.get('kid'):
			form = SellForm(request.GET, instance=post)
			if form.is_valid():
				form.save()
				messages.success(request, 'Post Updated Successfully')
				return redirect('useradds')
		return redirect('sell')
	student_id = Signup.objects.get(student_id=request.session['user_id_session_login'])
	form = SellForm()
	if request.method == 'POST':
		form = SellForm(request.POST)
		c_id = request.POST.get('student')
		c_stu_id = Signup.objects.get(id=c_id)
		if c_stu_id.student_id != student_id :
			return HttpResponse("<strong>Please Select You User Id to Post Add.</strong><br><a href='sell'><button>Click Hare To Try again</a>")
		if form.is_valid():
			form.save()
			return redirect('sellpost')
	context= {'form':form}
	return render(request,'bsi/sell.html',context)

def buy(request):
	if not request.session.has_key('user_id_session_login'):
		return redirect('login')
	items = Item.objects.all()
	context={ 'items' : items}
	return render(request,'bsi/alladds.html',context)

def sellpost(request):
	if not request.session.has_key('user_id_session_login'):
		return redirect('login')
	return render(request,'bsi/sellpost.html')

def useradds(request):
	if not request.session.has_key('user_id_session_login'):
		return redirect('login')
	id = Signup.objects.get(student_id=request.session['user_id_session_login'])
	items = Item.objects.filter(student=id)
	return render(request,'bsi/useradds.html',{'items':items})

def alladds(request):
	if not request.session.has_key('user_id_session_login'):
		return redirect('login')
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
	if not request.session.has_key('user_id_session_login'):
		return redirect('login')
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


# -------------------(DELETE VIEWS) -------------------

def deletePost(request):
	if not request.session.has_key('user_id_session_login'):
		return redirect('login')
	myid = request.GET.get('kid')
	print(myid)
	return HttpResponse(myid)
	# if request.method == "GET" and request.GET.get('kid'):
	# 	myid = request.GET.get('kid')
	# 	post = Item.objects.get(id=myid)
	# 	post.delete()
	# 	messages.success(request,'Post Deleted Succesfully')
	# 	return redirect(useradds)
	#
	# return render(request, 'accounts/delete_item.html', {'item': post})