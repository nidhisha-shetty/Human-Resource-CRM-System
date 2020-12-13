from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
# Create your models here.
class Pricebaba(models.Model):
	first_name = models.CharField(max_length=100, null=False);
	last_name = models.CharField(max_length=100, null=False);
	email = models.EmailField(max_length = 254); 
	mobile = models.IntegerField(validators=[MinValueValidator(7000000000), MaxValueValidator(9999999999)], null=False);
	age = models.IntegerField(max_length=100, null=False);	
	dob =  models.DateField();
	location = models.CharField(max_length=100, null=False);

	def details_edit(self):
		return f"/user_edit/{self.id}/"	