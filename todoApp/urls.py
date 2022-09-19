from django.urls import path
from .views import list_tasks, create_tasks


urlpatterns = [
    path('', list_tasks, name="main_page"),
    path('/new_task/', create_tasks, name="create_new_task")
]