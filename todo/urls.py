from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('submit',views.submit,name='submit'),
    path('list',views.list,name='list'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete_all/', views.delete_all, name='delete_all'),
]