from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view_logic(req):
    username = req.session.get('username')
    return render(req, 'index.html', {'username': username})
