from django.shortcuts import render
from .models import (Question,Choice)
from django.views.generic import DetailView,ListView

def owner(request):
    return render(request,'owner.html')
class IndexView(ListView):
    template_name = "index_list.html"
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]
    

class QuestionDetailView(DetailView):
    model=Question
    template_name="question_detail.html"
    pk_url_kwarg = "question_id"



class ResultsView(DetailView):
    model = Question
    template_name = "results_detail.html"
    pk_url_kwarg = "question_id"


def vote(request, question_id):
    return render(request,"You're voting on question %s." % question_id)
