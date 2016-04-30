from django.http import HttpResponse


def index(request):
    return HttpResponse('some hardcoded index return')