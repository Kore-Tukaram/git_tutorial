from django import forms
from .models import Info

class InfoForm(forms.ModelForm):#When inserting new data
	name = forms.CharField(widget = forms.TextInput(attrs = {
				"placeholder":"Enter your name",
				"class":"form-control"}))

	uid = forms.IntegerField(widget = forms.NumberInput(attrs={
				"placeholder":"Enter your uid",
				"class":"form-control"}))

	email = forms.EmailField(widget = forms.EmailInput(attrs={
				"placeholder":"Enter your email",
				"class":"form-control"}))
	gen = [('M',"Male"),("F","Female"),("O","Other")]
	gender = forms.ChoiceField(choices=gen, widget= forms.RadioSelect())

	location = forms.CharField(widget = forms.TextInput(attrs = {
				"placeholder":"Enter your location",
				"class":"form-control"}))
	cou=[("I","India"),("O","Other")]
	country = forms.ChoiceField(choices=cou, widget= forms.Select(attrs={"class":"form-control"}))

	class Meta:
		model=Info
		fields= "__all__"

class UpdateForm(forms.Form):
	uid = forms.IntegerField(widget = forms.NumberInput(attrs={
				"placeholder":"Enter your uid",
				"class":"form-control"}))

	name = forms.CharField(widget = forms.TextInput(attrs = {
				"placeholder":"Enter your new name",
				"class":"form-control"}))

class DeleteForm(forms.Form):
	uid = forms.IntegerField(widget = forms.NumberInput(attrs={
				"placeholder":"Enter uid to delete record",
				"class":"form-control"}))


