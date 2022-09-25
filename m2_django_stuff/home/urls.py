from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addTodoItem/', views.addTodoView, name='addTodoView'),
    path('deleteTodoItem/<int:i>/', views.deleteTodoView, name='deleteTodoView'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('updateitem/<int:i>', views.updateitem, name='updateitem'),
    path('register/', views.register, name='register')

]
