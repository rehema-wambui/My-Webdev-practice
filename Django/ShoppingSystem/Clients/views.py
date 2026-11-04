from django.shortcuts import render

# Create your views here.
def client_info(request):
    return render(request, 'client_info.html')