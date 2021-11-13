from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choise
from django.template import loader
from django.urls import reverse
from django.views import generic

# def index(request):
#     latest_question_list = Question.objects.order_by("id")[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     # output = ', '.join([latest_question_list.text for q in q_set])
#     return render(request, 'polls/index.html', context)
#
# def detail(request, question_id):
#
#     question = get_object_or_404(Question, pk = question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
# def results(request, question_id):
#
#     question = get_object_or_404(Question, pk=question_id)
#
#     return render(request, 'polls/results.html', {'question':question})
#
#     # return HttpResponse("question %s results" % question_id)


class IndexView(generic.ListView):
    model = Question
    # template_name = "polls/index.html"
    # context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    # template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):

    try:

        question = get_object_or_404(Question, pk=question_id)
        choise = get_object_or_404(Choise, pk=request.POST['choise'])

    except (KeyError, Choise.DoesNotExist):

        error_message = "Invalid choise id"
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': error_message,
        })

    except (Question.DoesNotExist):

        error_message = "Invalid question id %" % question_id
        return render(request, 'polls/detail.html', {
        'question': question,
        'error_message': error_message,
        })

    choise.votes += 1
    choise.save()

    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
