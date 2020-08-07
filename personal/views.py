from django.shortcuts import render
from personal.models import Question


# Create your views here.
def home(request):
	# print(request.headers)
	context={}
	# context['text']="Passing view data"
	# list_of_values=[]
	# list_of_values.append("First")
	# list_of_values.append("Second")
	# list_of_values.append("Third")
	# list_of_values.append("Fourth")
	# context['list_of_values']=list_of_values
	questions=Question.objects.all()
	context['questions']=questions

	return render(request, "personal/home.html",context)