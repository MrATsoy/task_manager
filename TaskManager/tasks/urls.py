from django.urls import path
from .views import *

urlpatterns = [
    path('category/<int:c_id>', tasks, name='tasks'),
    path('category/task/<int:task_id>/del', task_del, name='task_del'),
    path('category/task/<int:task_id>', description, name='desc'),
    path('add_category', add_category, name='add_c'),
    path('category/<str:category>/add_task', add_task, name='add_task'),
    path('', home, name='home')
]