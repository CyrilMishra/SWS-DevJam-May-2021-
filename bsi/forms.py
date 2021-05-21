from django.forms import ModelForm
from .models import Item



class SellForm(ModelForm):
	class Meta:
		model= Item
		# field = [ 'customer' , 'product']
		fields = '__all__' ;


class SellUpdateForm(ModelForm):
	class Meta:
		model = Item
		exclude=('student',)