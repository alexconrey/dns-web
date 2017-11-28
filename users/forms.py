from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile

class RegisterForm(UserCreationForm):
	domain = forms.CharField(max_length=64, help_text='Required for account creation.')

	class Meta:
		model = User
		fields = ('username', 'password1', 'password2', 'domain', )


class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', )

class ProfileForm(forms.ModelForm):
	email = forms.EmailField(max_length=64)
	bio = forms.CharField(max_length=255)
	class Meta:
		model = Profile
		fields = ('email', 'bio',)
	
	def clean(self):
		cleaned_data = super(ProfileForm, self).clean()
		email = cleaned_data.get("email")
		bio = cleaned_data.get("bio")

		if not email:
			self.add_error('email', forms.ValidationError('Email not set'))
		if not bio:
			self.add_error('bio', forms.ValidationError('Bio not set'))

	
