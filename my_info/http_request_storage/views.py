from models import HttpRequestStorage
from django.shortcuts import render


def main(request):
    return render(request, 'http_request_storage/main.html')
    
def requests(request):
    first_requests = HttpRequestStorage.objects.all().order_by('-date')[:10]
    context = {'first_requests': first_requests}
    return render(request, 'http_request_storage/requests.html', context)
