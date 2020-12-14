from django.urls import path
from todolist_app import views

urlpatterns = [
    # if view's real name got modified,
    # then you can use the name provided here instead of changing the view name throughout the whole project
    path('', views.todolist, name='todolist'),
    path('delete/<task_id>', views.delete_task, name='delete_task'),
    path('edit/<task_id>', views.edit_task, name='edit_task'),
    path('complete/<task_id>', views.complete_task, name='complete_task'),
]
