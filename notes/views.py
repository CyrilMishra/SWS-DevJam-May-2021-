from django.shortcuts import redirect, render, HttpResponse
from notes.forms import DocumentForm
from notes.models import Document, Course
from register.views import *
from community.views import *
from bsi.views import *
from lfi.views import *


def home(request):
    courses = Course.objects.all()
    return render(request, 'home.html', {'courses': courses})


def course_file(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'course_file.html', {'course': course})


def view_files(request, pk):
    course = Course.objects.get(pk=pk)

    documents = Document.objects.filter(course_name=course.name)
    return render(request, 'view_files.html', {'documents': documents})

def upload_file(request,pk):

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_files',pk)
    else:
        form = DocumentForm()
    return render(request, 'upload_file.html', {'form': form})



