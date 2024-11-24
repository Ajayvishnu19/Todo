from django.urls import path
from .import views

app_name='todoapp'
urlpatterns = [
    path('', views.add,name='add'),
    path('detail/<int:taskid>/',views.detail,name='detail'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
]