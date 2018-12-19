from django import forms
from .models import Items
from .models import userComments

class ItemsForm(forms.ModelForm):
	class Meta:
		model = Items
		fields= ["item","Description","ItemImage"]

class ContactForm(forms.Form):
    fullname = forms.CharField()
    email = forms.CharField()
    contact = forms.CharField()

class userCommentsForm(forms.ModelForm):
    class Meta:
    	model = userComments
    	fields= ["fullName","mobileNo","city","message"]