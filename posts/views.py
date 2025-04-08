from django.shortcuts import render, HttpResponse

# Create your views here.
def test_view (request):
    return HttpResponse('httpResponse')


def html_view (request):
    return render(request, 'base.html')