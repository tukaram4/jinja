from django.shortcuts import render

# Create your views here.
def jinja(request):
    d={'name':'ravi','age':'23'}
    return render(request,'jinja.html',context=d)