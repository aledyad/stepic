from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login

from models import Question
from forms import AskForm, AnswerForm, SignupForm

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


def question_details(request, q_id):
    question = get_object_or_404(Question, pk=q_id)
    answers = question.answer_set.all

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.cleaned_data['author'] = request.user
            form.cleaned_data['question'] = question
            answer = form.save()
            url = answer.question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm({'question': q_id})
    return render(request, 'question.html', {'question': question, 'answers': answers, 'form': form})


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


def add_question(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            form.cleaned_data['author'] = request.user
            ask = form.save()
            url = ask.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'question_form.html', {
        'form': form
    })


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup_form.html', {
        'form': form
    })
