from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def index(request):
    questions = Question.objects.all()
    context = {
        'questions': questions
        }
    return render(request, 'eithers/index.html', context)

def create(request):
    form = CreateModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('eithers:index')
    context = {
        'form': form
        }
    return render(request, 'eithers/create.html', context)

def detail(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    comment_form = CommentForm()

    context = {
        'question': question,
        'comment_form': comment_form,
        }
    return render(request, 'eithers/detail.html', context)

def comment(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    comment_form = CommentForm(request.POST or None)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.question = question
        comment.save()
        return redirect('eithers:detail', question_pk=question_pk)
    context = {
        'question': question,
        'comment_form': comment_form,
        }
    return render(request, 'eithers/detail.html', context)