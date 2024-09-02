
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def sum(request):
    # Get parameters from the request
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')

    # Ensure the parameters are not None
    if num1 is None or num2 is None:
        return HttpResponse("Invalid input", status=400)

    # Convert parameters to integers
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        return HttpResponse("Invalid numbers", status=400)

    # Perform the sum operation
    result = num1 + num2
    params = {'sum': result}

    return render(request, 'results.html', params)

