

from django.http import HttpResponse

def index(request):
    return HttpResponse(" Hello you are viewing Django local page ")
