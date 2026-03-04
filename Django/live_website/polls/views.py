from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from polls.models import Question


# Create your views here.
def hello(request):
	return render(request, "polls/index.html")

def home(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]

    context = {
        "questions": latest_questions,
    }
    return render(request,
                  "polls/list_questions.html",
                  context)