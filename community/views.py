import register
from django.shortcuts import render, HttpResponse
from datetime import datetime
from .models import CommunityQuestion, CommunityAnswer
from register.models import Signup
from register.views import login
# Create your views here.
# Community
class Manage_Post():
    def __init__(self, name, question_description ,question_id):
        self.name = name
        self.question_description = question_description
        self.id = question_id
def EditPost(request):

    if request.method == "POST" and request.POST.get('updatepass'):
        qid = request.POST.get('updatepass')
        data = CommunityQuestion.objects.get(question_id=qid)
        data.question_description = request.POST.get('EditQuestion')
        data.save()
    qid = request.GET.get('qid')
    data = CommunityQuestion.objects.get(question_id=qid)
    context={
        "data":data
    }
    return render(request,'editpost.html',context)
def ManagePost(request):
    a=10
    ids = request.session['user_id_session_login']
    data_ids = Signup.objects.get(student_id=ids)
    data = CommunityQuestion.objects.filter(student_id=data_ids)[:a]

    context={
        "data":data,
        "data_ids":data_ids,
    }

    if request.method == "POST" and request.POST.get('delete'):
        questionid = request.POST.get('delete')
        CommunityQuestion.objects.get(question_id=questionid).delete()

    return render(request,'ManagePost.html',context)

def logout(request):
    try:
        del request.session['user_id_session_login']
    except:
        pass
    else:
        return HttpResponse("<strong>You are logged out.</strong><br><a href='login'>click here to login</a>")

class Com():
    def __init__(self, student_id, stu_name, question_id, question_description,):
        self.student_id = student_id
        self.stu_name = stu_name
        self.question_id = question_id
        self.question_description = question_description
def community(request):

    my_obj_list = []
    if request.method == "POST" and request.POST.get('showmore'):
        a=int(request.POST.get('showmore'))
        a=int(a+5)
        data = CommunityQuestion.objects.all()[:a]
        for x in data:
            name = Signup.objects.get(student_id=x.student_id)
            obj = Com(x.student_id, name.name, x.question_id, x.question_description)
            my_obj_list.append(obj)
        for x in my_obj_list:
            print(x.stu_name)
    else:
        a=5;
        data = CommunityQuestion.objects.all()[:a]
        for x in data:
            name = Signup.objects.get(student_id=x.student_id)
            obj = Com(x.student_id, name.name, x.question_id, x.question_description)
            my_obj_list.append(obj)
        for x in my_obj_list:
            print(x.stu_name)
    #print(data)
    context = {
        "student_question" : my_obj_list,
        "a": a,
    }
    if request.method == "GET" and request.GET.get('subque'):
        qid = request.GET.get('subque')
        ans = request.GET.get('answer')
        print(qid)
        print(ans)
        ids=request.session['user_id_session_login']
        query_question = CommunityQuestion.objects.get(question_id=qid)
        query_User_id = Signup.objects.get(student_id =ids )
        ans_obj =CommunityAnswer(question_id=query_question, student_id= query_User_id, answer_discrption = ans)
        ans_obj.save()
    if request.method == "POST" and request.POST.get('post_question'):
        # print(request.POST.get('Question'))
        question = request.POST.get('Question')
        dep = request.POST.get('option')
        ids = request.session['user_id_session_login']
        Myid = Signup.objects.get(student_id=ids)
        name = Myid.name
        communityQuestion = CommunityQuestion(stu_name=name, student_id=Myid, question_description=question,
                                              publishing_date=datetime.today(), stu_department=dep)
        communityQuestion.save()

    return render(request, 'community.html', context)


# Profile
def profile(request):
    if request.method == "POST" and request.POST.get('update_pass'):
        print(request.POST.get('update_pass'))
        context = {
        }
        return render(request, 'updatepass.html' , context)
    if request.method == "POST" and request.POST.get('updateinfo'):
        #print(request.POST.get('updateinfo'))
        stid = request.POST.get('student_id')
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        mobile = request.POST.get('mobilenumber')
        print(stid)
        obj_users = Signup.objects.get(student_id=stid)
        obj_users.name = name
        obj_users.gender = gender
        #obj_users.dob = dob
        obj_users.mobile_number=mobile
        obj_users.save()
    if  request.method =="GET" and request.GET.get('pid') :
        myid = request.GET.get('pid')
        data = Signup.objects.get(student_id=myid)
        context = {
            "info": data
        }
        return render(request, 'profiles.html', context)
    else:
        ids = request.session['user_id_session_login']
        Myid = Signup.objects.get(student_id=ids)
        context = {
            "info" : Myid
        }
        return render(request, 'profile.html', context)


# communityanswer
class Com_Ans():
    def __init__(self,answer_id, name ,answer_discrption ,upvote ,downvote ):
        self.answer_id = answer_id
        self.name = name
        self.answer_discrption = answer_discrption
        self.upvote = upvote
        self.downvote = downvote

def communityanswer(request):
    if request.method == "POST" and request.POST.get('showmore'):
        a = int(request.POST.get('showmore'))
        a = int(a+5)
        mydata = []
        mykey = request.GET.get('key')
        question_data = CommunityQuestion.objects.get(question_id=mykey)
        data = CommunityAnswer.objects.filter(question_id=mykey)[:a]
        for x in data:
            check_id = x.student_id
            check_data = Signup.objects.get(student_id=check_id)
            check_question_desciption = x.answer_discrption
            obj = Com_Ans(x.answer_id, check_data.name, check_question_desciption, x.upvote, x.downvote)
            mydata.append(obj)
    else:
        a=5
        mydata = []
        mykey = request.GET.get('key')
        question_data = CommunityQuestion.objects.get(question_id=mykey)
        data = CommunityAnswer.objects.filter(question_id=mykey)[:a]
        for x in data:
            check_id = x.student_id
            check_data = Signup.objects.get(student_id=check_id)
            check_question_desciption = x.answer_discrption
            obj = Com_Ans(x.answer_id, check_data.name, check_question_desciption, x.upvote, x.downvote)
            mydata.append(obj)

    context = {
        "question_data": question_data,
        "answer_data": mydata,
        "a" : a,
    }
    if request.method == "POST" and request.POST.get('upvote'):
        ansid = request.POST.get('upvote')
        obj_answer = CommunityAnswer.objects.get(answer_id=ansid)
        up = int(obj_answer.upvote);
        up = int(up+1)
        obj_answer.upvote=up;
        obj_answer.save();
        return render(request, 'communityanswer.html', context)
    if request.method == "POST" and request.POST.get('downvote'):
        ansid = request.POST.get('downvote')
        obj_answer = CommunityAnswer.objects.get(answer_id=ansid)
        dow = int(obj_answer.downvote)
        dow = int(dow+1)
        obj_answer.downvote=dow;
        obj_answer.save();
        return render(request, 'communityanswer.html', context)

    if request.method == "POST" and request.POST.get('submitAnswer'):
        if request.POST.get('file'):
            file = request.POST.get('file')
            stuid = request.session['user_id_session_login']
            ansdes= request.POST.get('answer_discription')
            qid=request.GET.get('key')
            data_quuestion = CommunityQuestion.objects.get(question_id=qid)
            data_student = Signup.objects.get(student_id=stuid)
            cmans = CommunityAnswer(question_id=data_quuestion, student_id=data_student, answer_discrption=ansdes, answer_assets=file)
            cmans.save()
        else:
            #file = request.POST.get('file')
            stuid = request.session['user_id_session_login']
            ansdes = request.POST.get('answer_discription')
            qid = request.GET.get('key')
            data_quuestion = CommunityQuestion.objects.get(question_id=qid)
            data_student = Signup.objects.get(student_id=stuid)
            cmans = CommunityAnswer(question_id=data_quuestion, student_id=data_student, answer_discrption=ansdes)
            cmans.save()
        #answer_discription
        return render(request, 'communityanswer.html', context)
    elif request.method == "GET" and request.GET.get('key') :
        #mykey = request.GET.get('key')
        #question_data = CommunityQuestion.objects.get(question_id=mykey)
        #data = CommunityAnswer.objects.filter(question_id=mykey)
        #context = {
        #     "question_data" : question_data,
        #     "answer_data" : data
        #}
        return render(request, 'communityanswer.html', context)
    return render(request, 'communityanswer.html',context)