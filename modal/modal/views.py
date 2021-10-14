from django.shortcuts import render

# Create your views here.

def stream(request):
    context = {'value' : 1}
    return render(request, 'stream.html',context)

def base(request):
    return render(request, 'base.html')

def iframe1(request):
    return render(request, 'iframe1.html')

def iframe2(request):
    return render(request, 'iframe2.html')

def iframe3(request):
    return render(request, 'iframe3.html')