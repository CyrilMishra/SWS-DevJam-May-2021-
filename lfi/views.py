#from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import views
from .models import *
import community
from community.views import search
from .forms import *


# Create your views here.
class Match():
    def __init__(self, name  , description , founded_by , course ,match_percent):
        self.name = name
        self.description = description
        self.founded_by = founded_by
        self.course = course
        self.match_percent = match_percent


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
    student_id = Signup.objects.get(student_id=request.session['user_id_session_login'])

    form = LostForm()
    if request.method == 'POST':
        # print('Printing_POST :',request.POST)
        form = LostForm(request.POST)
        c_id = request.POST.get('student')
        c_stu_id = Signup.objects.get(id=c_id)
        # print(c_id)
        # print(c_stu_id)
        # print(student_id)
        if c_stu_id != student_id:
            return HttpResponse(
                "<strong>Please Select You User Id to Post Add.</strong><br><a href='foundreport'><button>Click Hare To Try again</a>")

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
    student_id = Signup.objects.get(student_id=request.session['user_id_session_login'])

    form = FoundForm()
    if request.method == 'POST':
        # print('Printing_POST :',request.POST)
        form = FoundForm(request.POST)
        c_id = request.POST.get('student')
        c_stu_id = Signup.objects.get(id=c_id)
        # print(c_id)
        # print(c_stu_id)
        # print(student_id)
        if c_stu_id != student_id:
            return HttpResponse(
                "<strong>Please Select You User Id to Post Add.</strong><br><a href='foundreport'><button>Click Hare To Try again</a>")

        if form.is_valid():
            form.save()
            return redirect('founditemadded')
    context = {'form': form}
    return render(request, 'lfi/foundreport.html', context)


def lostentryadded(request):
    return render(request, 'lfi/lostentryadded.html')


def founditemadded(request):
    return render(request, 'lfi/founditemadded.html')




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
    student_id = Signup.objects.get(student_id=request.session['user_id_session_login'])

    report = LostItem.objects.get(id=pk)
    # print(pk)
    form = LostForm(instance = report)
    if request.method == 'POST':
        form = LostForm(request.POST, instance=report)
        c_id = request.POST.get('student')
        c_stu_id = Signup.objects.get(id=c_id)
        # print(c_id)
        # print(c_stu_id)
        # print(student_id)
        if c_stu_id != student_id:
            return HttpResponse(
                "<strong>Please Select You User Id to Post Add.</strong><br><a href=''><button>Click Hare To Try again</a>")

        if form.is_valid():
            form.save()
            return redirect('userslostentries')
    context = {'form': form}
    return render(request, 'lfi/lostreport.html', context)


def foundreportupdate(request,pk):
    student_id = Signup.objects.get(student_id=request.session['user_id_session_login'])

    report = FoundItem.objects.get(id=pk)
    # print(pk)
    # form = FoundForm()
    form = FoundForm(instance = report)
    if request.method == 'POST':
        form = FoundForm(request.POST, instance=report)
        c_id = request.POST.get('student')
        c_stu_id = Signup.objects.get(id=c_id)
        # print(c_id)
        # print(c_stu_id)
        # print(student_id)
        if c_stu_id != student_id:
            return HttpResponse(
                "<strong>Please Select You User Id to Post Add.</strong><br><a href=''><button>Click Hare To Try again</a>")

        if form.is_valid():
            form.save()
            return redirect('userfoundentries')
    context = {'form': form}
    return render(request, 'lfi/foundreport.html', context)



def matchpageresult(request,pk):
    oneitem = LostItem.objects.get(id=pk)
    allitem = FoundItem.objects.all()
    stu_id1 = oneitem.student_id
    item_name1 = oneitem.item_name
    item_price1 = oneitem.item_price
    item_desc1 = oneitem.item_description
    item_type1 = oneitem.item_type
    lost_place1 = oneitem.lost_place
    lost_time1 = oneitem.lost_time
    lost_date1 = oneitem.lost_date
    item_color1 = oneitem.item_color
    company_type1 = oneitem.company_type
    item_shape1 = oneitem.shape
    author_name1 = oneitem.author_name
    fg=[]
    for i in allitem :
        stu_id = i.student
        z=0
        if i.item_name == item_name1:
            z+=1
        if i.item_price == item_price1:
            z+=1
        if i.found_place == lost_place1 :
            z+=1
        if i.shape == item_shape1 :
            z+=1
        if i.item_type == item_type1:
            z += 1
        if i.found_time == lost_time1:
            z += 1
        if i.found_date == lost_date1 :
            z+=1
        if i.company_type == company_type1 :
            z+=1
        if i.author_name == author_name1 :
            z+=1
        if i.item_color == item_color1 :
            z+=1
        if i.item_description ==  item_desc1 :
            z+=1
        sd = round((z/11 * 100),2)
        fb = Signup.objects.get(student_id=i.student)
        stu_name = fb.name
        stu_course = fb.course
        obj = Match(item_name1, item_desc1,stu_name,stu_course,sd)
        fg.append(obj)

    context = {'mi':fg}
    return render(request,"lfi/matchpageresult.html",context)