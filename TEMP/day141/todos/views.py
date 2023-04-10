from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo

# Create your views here.

def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }


    return render(request, 'todos/index.html', context)


def create(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        form = form.save(commit=False)
        form.author = request.user
        form.save()
        return redirect('todos:index', )
    
    context = {
        'form': form,
    }
    return render(request, 'todos/create.html', context)


def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('todos:index', )

def toggle(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todos:index', )