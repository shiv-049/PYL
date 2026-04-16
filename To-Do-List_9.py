Step 1: Install Django

Open Terminal:

pip install django
🔹 Step 2: Create Project
django-admin startproject todoApp
cd todoApp
🔹 Step 3: Create App
python manage.py startapp todos
🔹 Step 4: Register App

Open settings.py and add:

INSTALLED_APPS = [
    'todos',
]
🔹 Step 5: Create Model (models.py)
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
🔹 Step 6: Migrate Database
python manage.py makemigrations
python manage.py migrate
🔹 Step 7: Create Views (views.py)
from django.shortcuts import render, redirect
from .models import Task

def index(request):
    tasks = Task.objects.all()

    if request.method == "POST":
        title = request.POST.get('title')
        Task.objects.create(title=title)
        return redirect('/')

    return render(request, 'index.html', {'tasks': tasks})

def complete(request, id):
    task = Task.objects.get(id=id)
    task.completed = True
    task.save()
    return redirect('/')

def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('/')
🔹 Step 8: Create URLs
todos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('complete/<int:id>/', views.complete),
    path('delete/<int:id>/', views.delete),
]
project urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todos.urls')),
]
🔹 Step 9: Create Template

Create folder:

mkdir -p todos/templates

Create index.html:

<!DOCTYPE html>
<html>
<head>
    <title>To-Do List</title>
</head>
<body>

<h1>To-Do List</h1>

<form method="POST">
    {% csrf_token %}
    <input type="text" name="title" placeholder="Enter task">
    <button type="submit">Add</button>
</form>

<ul>
{% for task in tasks %}
    <li>
        {% if task.completed %}
            <strike>{{ task.title }}</strike>
        {% else %}
            {{ task.title }}
        {% endif %}

        <a href="/complete/{{task.id}}">Complete</a>
        <a href="/delete/{{task.id}}">Delete</a>
    </li>
{% endfor %}
</ul>

</body>
</html>
🔹 Step 10: Run Server
python manage.py runserver
🔹 Step 11: Open Browser

👉 Go to:

http://127.0.0.1:8000
