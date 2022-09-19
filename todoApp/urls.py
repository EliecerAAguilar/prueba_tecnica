from django.urls import path
from .views import list_tasks, create_tasks, delete_task, update, updated_task

urlpatterns = [
    path('', list_tasks, name="main_page"),
    path('new_task/', create_tasks, name="create_new_task"),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
    path('update_task/<int:task_id>/', update, name='update'),
    path('updated_task/<int:task_id>/', updated_task, name='updated_task'),
]