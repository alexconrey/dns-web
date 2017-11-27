from django.forms import ModelForm, Textarea
from django.contrib.auth.models import User

class RegisterForm(ModelForm):
	class Meta:
		model = User
		fields = ("username",)

