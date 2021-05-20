import register
from django.shortcuts import render, HttpResponse
from register.models import Signup
from .models import Message, ChatTransaction
from datetime import datetime
# Create your views here.
class myobject():
    def __init__(self,id,name,msg):
        self.id = id
        self.name = name
        self.msg = msg


class MessageClass():
    def __init__(self, id, name, message):
        self.id = id
        self.name = name
        self.message = message



def converstion(request):

    if request.method == "POST" and request.POST.get('send'):
        message = request.POST.get('message')
        sdid = request.POST.get('send')
        # needs to be given by sesseion
        id = "2020ca033"
        ss = Signup.objects.get(student_id=id)
        ds = Signup.objects.get(student_id=sdid)
        if (ChatTransaction.objects.filter(s=ss) & ChatTransaction.objects.filter(d=sdid)) or (ChatTransaction.objects.filter(s=ds) & ChatTransaction.objects.filter(d=id)):
            data = ((ChatTransaction.objects.filter(s=ss) & ChatTransaction.objects.filter(d=sdid)) | (ChatTransaction.objects.filter(s=ds) & ChatTransaction.objects.filter(d=id)))
            sdata = data[0]
            print(sdata)
            obj_tr = Message(s=ss, d=sdid, transaction_id=sdata, message=message, time=datetime.now().time())
            obj_tr.save()

            sdata.time=datetime.now().time()
            sdata.save()
        else:
            obj = ChatTransaction(s=ss, d=sdid, time=datetime.now().time())
            obj.save()
            obj_tr = Message(s=ss, d=sdid, transaction_id=obj, message=message, time = datetime.now().time())
            obj_tr.save()





    sdid = request.GET.get('sdid')
    #needs to be tken from Session
    id= "2020ca033"
    con_data= []
    ss = Signup.objects.get(student_id=id)
    ds = Signup.objects.get(student_id=sdid)
    data_message = (Message.objects.filter(s=ss).order_by('time') & Message.objects.filter(d=sdid)).order_by('time') | (Message.objects.filter(s=ds).order_by('time') & Message.objects.filter(d=id)).order_by('time')
    for x in data_message:
        print(x.message)
        name = Signup.objects.get(student_id=x.s)
        #message = x.message
        id =x.s
        obj = MessageClass(id,name.name,x.message)
        con_data.append(obj)
    context={
        "dsname":ds,
        "message": con_data,
    }

    return render(request, 'conversation.html', context)
def chatapp(request):

    #chatapp brings session vvraiable
    # code need to removed when you get session
    Myid ='2020ca033'
    ss = Signup.objects.get(student_id=Myid)
    d = ChatTransaction.objects.filter(s = ss ).order_by('-time') | ChatTransaction.objects.filter(d = Myid).order_by('-time')

    #p1 = myobject(Myid,ss.name)
    s = []
    for x in d:
        my =str(x.s)
        el =str(x.d)
        if my != Myid:
            print(type(x.s))
            print(type(Myid))
            print("if block")
            print(x.s)

            fi = Signup.objects.get(student_id=x.s)
            msg = Message.objects.filter(s=x.s).last()
            obj = myobject(x.s, fi.name, msg.message)
            s.append(obj)
        elif  el != Myid:
            print(type(x.d))
            print(type(Myid))
            print("elseif block")
            print(x.d)
            fi = Signup.objects.get(student_id=x.d)
            msg = Message.objects.filter(s=x.s).last()
            obj = myobject(x.d, fi.name, msg.message)
            s.append(obj)
    print(s)
    for x in s:
        print(x.id)
        print(x.name)
    context = {
        "mydata": s
    }
    return render(request, 'message.html', context)
