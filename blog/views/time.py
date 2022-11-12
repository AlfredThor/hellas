from django.shortcuts import render
from django.views.generic import View


class Time(View):

    def get(self, request):
        return render(request, 'time.html')