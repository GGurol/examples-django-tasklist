# All imports are now from their modern locations
from django.shortcuts import render, redirect
from django.core.cache import cache
from .models import Task

# A constant for our cache key
TASKS_KEY = "tasks.all"

def index(request):
    """
    Fetches the list of tasks from the cache.
    If not in the cache, it queries the database, then stores the result in the cache.
    """
    tasks = cache.get(TASKS_KEY)
    if tasks is None:
        # The query is only run if the cache is empty
        tasks = Task.objects.order_by("id")
        # Store the result in the cache for future requests
        cache.set(TASKS_KEY, tasks)
    
    # Use the modern `render` function
    return render(request, 'index.html', {'tasks': tasks})

def add(request):
    """
    Adds a new task and invalidates the cache.
    """
    if request.method == 'POST':
        Task.objects.create(name=request.POST.get("name"))
        # Invalidate the cache by deleting the key. The next visit to index() will refresh it.
        cache.delete(TASKS_KEY)
    return redirect("/")

def remove(request):
    """
    Removes a task and invalidates the cache.
    """
    if request.method == 'POST':
        task_id = request.POST.get("id")
        Task.objects.filter(id=task_id).delete()
        # Invalidate the cache by deleting the key.
        cache.delete(TASKS_KEY)
    return redirect("/")
