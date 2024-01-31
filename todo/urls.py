from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('submit/',views.submit,name='submit'),
    path('list/',views.list,name='list'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete_all/', views.delete_all, name='delete_all'),
    path('user_login/',views.user_login,name='user_login'),
    path('signup/',views.create_user,name='create_user'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
]