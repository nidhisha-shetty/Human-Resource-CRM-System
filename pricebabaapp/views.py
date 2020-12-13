from django.shortcuts import render
from .forms import Pricebabaf
from django.contrib import messages
from .models import Pricebaba
from django.views.generic import ListView
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def add_view(request):
	form=Pricebabaf(request.POST or None)
	if form.is_valid():
		form.save()
		form=Pricebabaf()
		messages.info(request, "User details added successfully!")
	context={
		'forming':form
		}
	return render(request, "emp_create.html", context)

def list_view(request):
    user=Pricebaba.objects.all()#.order_by("-emp_id") 
    
    context={
        'emp':user
    }
    return render(request, "record.html", context)

def edit_view(request, id):
    user=Pricebaba.objects.get(id=id)
    form=Pricebabaf(request.POST or None, request.FILES or None, instance=user)
    if form.is_valid():  
    	form.save()
    	messages.info(request, "User details changed successfully!")
    	form=Pricebabaf()
    context={
    	'user_form':form
    }
    return render(request, "edit.html", context)

class crudview(ListView):
    model = Pricebaba
    template_name = 'crud.html'
    context_object_name = 'users'
    paginate_by = 5