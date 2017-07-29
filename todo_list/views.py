from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from .models import TodoList
from .forms import TodoForm

# Create your views here.
def todo_listview(request):
	context 	= TodoList.objects.all()
	return render(request, 'todo_list/todo.html', {'todo':context})

# class TodoListView(View):
# 	def get(self, request, *args, **kwargs):
# 		context		= TodoList.objects.all()
# 		form 		= TodoForm()
# 		return render(request, 'todo_list/todo.html', {'todo':context, 'form':form})

# 	def post(self, request, *args, **kwargs):
# 		form = TodoForm(request.POST)
# 		if form.is_valid():
# 			name		= form.cleaned_data['name']
# 			entry 		= TodoList.objects.create(title=name)
# 			form 		= TodoForm()
# 			context 	= TodoList.objects.all()
# 			return render(request, 'todo_list/todo.html', {'form':form, 'todo':context})


# Using list view to return a view of lists
class TodoListView(ListView):
	template_name = 'todo_list/todo.html'

	def get_queryset(self):
		print(self.kwargs)
		slug = self.kwargs.get('slug')
		if slug:
			j = slug[0].upper() + slug[1:]
			queryset = TodoList.objects.filter(
					Q(title__startswith=j) |
					Q(title__icontains=j)
				)
		else:
			queryset = TodoList.objects.all()

		return queryset

class TodoListDetailView(DetailView):
	queryset = TodoList.objects.all()
	def get_context_data(self, *args, **kwargs):
		print(self.kwargs)
		context = super(TodoListDetailView, self).get_context_data(*args,**kwargs)
		print(context)
		return context
	def get_object(self, *args, **kwargs):
		td_id = self.kwargs.get('td_id')
		obj = get_object_or_404(TodoList, id=td_id) # can also use pk = td_id
		return obj

class SearchTodoListView(ListView):
	template_name = 'todo_list/todo.html'


