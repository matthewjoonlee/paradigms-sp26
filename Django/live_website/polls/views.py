from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from polls.models import Question


# Create your views here.
# def hello(request):
# 	return render(request, "polls/index.html")

# def hello(request):
# 	context = {"latest_questions": Question.objects.order_by("-pub_date")[:5]}
# 	return render(request, "polls/list_questions.html", context)

class IndexView(ListView):
    template_name = 'polls/list_questions.html'
    context_object_name = 'latest_questions'

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]
