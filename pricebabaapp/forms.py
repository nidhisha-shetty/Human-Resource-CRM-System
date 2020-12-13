from django import forms
from .models import Pricebaba

class DateInput(forms.DateInput):
    input_type = 'date'

class Pricebabaf(forms.ModelForm):
	class Meta:
		model = Pricebaba
		fields=[
			'first_name',
			'last_name',
			'email',
			'mobile',
			'age',
			'dob',
	 		'location'
		]
		widgets = {
            'dob': DateInput(),
        }
	