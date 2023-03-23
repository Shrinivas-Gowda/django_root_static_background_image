from django.shortcuts import render

# Create your views here.

def inception(request):
    return render(request,'index.html')
