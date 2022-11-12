from django.shortcuts import render
from django.views.generic import View


class Cover(View):

    def get(self, request):

        return render(request, 'cover.html')