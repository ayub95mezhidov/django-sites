from django.shortcuts import render
from .models import TodoListItem
from django.http import HttpResponseRedirect

def todoappView(request):
	all_todo_items = TodoListItem.objects.all()
	return render(request, 'todoapp/todolist.html', {'all_items' : all_todo_items})


def addTodoView(request):
	x = request.POST['content']
	new_item = TodoListItem(content = x)
	new_item.save()
	return HttpResponseRedirect('/todoapp/')


def deleteTodoView(request, i):
	y = TodoListItem.objects.get(id=i)
	y.delete()
	return HttpResponseRedirect('/todoapp/')
