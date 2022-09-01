from django.shortcuts import render
from django.contrib.auth.models import User
from .form import AmountForm
from .models import Amount
def pay(request,  *args, **kwargs):
	form = AmountForm()
	if request.method == 'POST':
	       
	       form = AmountForm(request.POST)
	       if form.is_valid():
	           amount = Amount(
                Amount = form.cleaned_data["Amount"],
             
                
            )
	           amount.save()
	           
            
	       
	context = {	
	'form':form,
	}
	return render(request,'pay/pay.html',context)
	
# Create your views here.
