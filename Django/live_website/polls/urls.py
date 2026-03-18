from django.urls import path
from polls.views import HomeView, QuestionView, vote, ResultsView

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path("", HomeView.as_view(), name="home"),
    # ex: /polls/5/
    path('<int:pk>/', QuestionView.as_view(), name="detail"),
    # ex: /polls/5/vote/
    path("<int:pk>/vote", vote, name="vote"),
    # TODO: /polls/5/results/
    path("<int:pk>/results/", ResultsView.as_view(), name="results"),
]