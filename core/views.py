from django.views.generic import View
from django.shortcuts import render

class HomeView():
    def get(self, request, *args, **kwargs):
        context = {
        }
        return render(request, 'index.html', context)