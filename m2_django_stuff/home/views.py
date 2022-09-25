from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from .models import TodoListItem
from .forms import TodoListItemForm
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def home(request):
    all_todo_items = TodoListItem.objects.all()
    context = {'all_items': all_todo_items}
    return render(request, 'index.html', context)


@login_required(login_url=login)
@permission_required('home.change_profile', login_url='login')
def addTodoView(request):
    x = request.POST['content']
    # print(x)
    new_item = TodoListItem(content=x)
    # print(new_item.content)
    new_item.save()
    messages.success(request, "Item added successfully")
    return redirect('home')


def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id=i)
    y.delete()
    messages.success(request, 'Item deleted successfully')
    return redirect('home')


def loginpage(request):
    if request.method == 'POST':
        username = request.POST['Name']
        password = request.POST['password']
        # print(username, password)
        user = authenticate(request, username=username, password=password)
        # Checks if the user exists in django db

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')


def logoutpage(request):
    print("log out")
    logout(request)
    return redirect('home')


def updateitem(request, i):
    mydataupdt = TodoListItem.objects.get(id=i)
    updateForm = TodoListItemForm(request.POST or None, instance=mydataupdt)
    if updateForm.is_valid():
        updateForm.save()
        messages.success(request, 'Todolist details updated.')
        return redirect('home')
    context = {"form": updateForm}
    messages.error(request, 'Invalid form.')
    return render(request, 'updateitem.html', context)


def register(request):
    if request.method == 'POST':
        user = request.POST['Name']
        email = request.POST['email']
        password1 = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if password1 == confirmpassword:
            if not User.objects.filter(username=user).exists():
                if not User.objects.filter(email=email).exists():
                    user = User.objects.create_user(
                        username=user, email=email, password=password1)
                    user.save()
        return redirect('login')
    return render(request, 'register.html')
