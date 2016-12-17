from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET

from models import Question

# Create your views here.


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def question_list_all(request):
    questions = Question.objects.new()
    page = paginate(request, questions)
    return render(request, 'questions.html', {
        'questions': page.object_list
    })


def popular_list_all(request):
    questions = Question.objects.popular()
    page = paginate(request, questions)
    return render(request, 'questions.html', {
        'questions': page.object_list
        })


@require_GET
def question_details(request, id):
    question = get_object_or_404(Question, pk=id)
    answers = question.answer_set.all
    return render(request, 'question.html', {'question': question, 'answers': answers})


def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page
