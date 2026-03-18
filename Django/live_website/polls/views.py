from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView


from polls.models import Question, Choice


# Create your views here.
def hello(request):
	return render(request, "polls/index.html")

def home(request):
    latest_questions = Question.objects.order_by('-pub_date')#[:5]

    context = {
        "questions": latest_questions,
    }
    return render(request,
                  "polls/question_list.html",
                  context)

class HomeView(ListView):
    model = Question
    paginate_by = 20
    context_object_name = "questions"


class QuestionView(DetailView):
    model = Question
    # template_name = "question_detail.html" (default)

def vote(request, pk):
    # retrieve question from DB
    question = get_object_or_404(Question, pk=pk)

    # retrieve choice from DB
    try:
        selected_choice_id = request.POST["choice"]
        print("selected_choice_id", selected_choice_id)
        choice = question.choice_set.get(pk=selected_choice_id)
        choice.votes += 1
        choice.save()

    # catch exception (KeyError, Choice.DoesNotExist) and display an error back to user
    except (KeyError, Choice.DoesNotExist):
        context = {
            "question": question,
            "error_message": "You didn't select a choice.",
        }
        return render(request,
                      "polls/question_detail.html",
                      context)

    # redirect user back to results page (polls:results)
    return HttpResponseRedirect(reverse("polls:results", args=(pk,)))


class ResultsView(DetailView):
    model = Question
    template_name = "polls/results.html"