from django.conf.urls import url
from .views import (
	TodoListView,
	TodoListDetailView
)


urlpatterns = [
	url(r'^$', TodoListView.as_view(), name="todo-list" ),
	#url(r'^(?P<slug>\w+)/', TodoListView.as_view()),
	url(r'^(?P<td_id>\w+)/', TodoListDetailView.as_view())
]