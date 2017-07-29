from django import forms

class TodoForm(forms.Form):
	name = forms.CharField(label="Task Name", max_length=100)
