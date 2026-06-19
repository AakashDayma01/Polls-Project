from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([str(q) for q in latest_question_list])

    return render(request, 'polls/index.html', context={"latest_question_list":latest_question_list})

def details(request, question_id):
	return HttpResponse("you are looking at questioon %s." % question_id)

def results(request, question_id):
	return HttpResponse("you are looking at result of question %s." % question_id)

def vote(request, question_id):
	return HttpResponse("you are voting on questioon %s." % question_id)