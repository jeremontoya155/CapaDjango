from django.shortcuts import render

# Create your views here.
def render_estaticos(request):
    return render(request,'estaticos.html')