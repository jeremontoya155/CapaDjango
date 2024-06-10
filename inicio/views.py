from django.shortcuts import render

# Create your views here.
def index_render(request):
    return render(request,'index.html')

