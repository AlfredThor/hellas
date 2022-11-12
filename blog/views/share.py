from django.shortcuts import render
from django.views.generic import View


class Share(View):

    def get(self, request):
        return render(request, 'share.html')