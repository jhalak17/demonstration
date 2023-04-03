from django.shortcuts import render
from django.views import View

# Create your views here.

class UserLogin(View):

    def get(self, request):
        return render(request, 'loginform.html')
    
    def post(self, request):
        print(request.POST)
