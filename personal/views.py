from django.shortcuts import render
from account.models import Account
# from personal.models import Question


# Create your views here.
def home(request):
# 	# print(request.headers)
	context={}
	account=Account.objects.all()
	context['accounts']=account

	return render(request, "personal/home.html",context)