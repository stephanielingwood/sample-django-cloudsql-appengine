from django.shortcuts import render
from storage import Storage

def greet(request):
  storage = Storage()
  storage.populate()
  score = storage.get_score()

  return render(request, 'index.html', {'score': score})

