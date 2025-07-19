from django.urls import path
from tasks.views import show_task
from tasks.views import show_specific_task
# from tasks.views import heda
urlpatterns=[
    path('show-task/',show_task),
    path('show-task/<int:id>',show_specific_task)
    # path('hedar-url',heda)
]