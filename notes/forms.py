from django import forms
from notes.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('course_name','subject', 'title', 'file')