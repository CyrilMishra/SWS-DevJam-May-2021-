from django.forms import ModelForm
from .models import *



class LostForm(ModelForm):
	class Meta:
		model = LostItem
		# field = [ 'customer' , 'product']
		fields = '__all__'


class FoundForm(ModelForm):
	class Meta:
		model = FoundItem
		# field = [ 'customer' , 'product']
		fields = '__all__'

class MatchForm(ModelForm):
	class meta:
		model = Matching
		fields = '__all__'