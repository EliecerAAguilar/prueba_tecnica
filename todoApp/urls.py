from django.urls import path
from .views import list_tasks, create_tasks,delete_task


urlpatterns = [
    path('', list_tasks, name="main_page"),
    path('/new_task/', create_tasks, name="create_new_task"),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task')
]