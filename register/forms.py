from django.forms import ModelForm
from .models import Signup



class SignupForm(ModelForm):
	class Meta:
		model= Signup
		# field = [ 'customer' , 'product']
		fields = '__all__'