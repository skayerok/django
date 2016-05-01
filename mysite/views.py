from django.http import HttpResponseRedirect


def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('books')
    else:
        return HttpResponseRedirect('login/')