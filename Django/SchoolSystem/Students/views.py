from django.shortcuts import render

# Create your views here.
def addstudent(request):
    return render(request, 'addstudent.html')