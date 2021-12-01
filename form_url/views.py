from django.shortcuts import render
from django.utils.crypto import get_random_string
# Create your views here.

def index(request):
    var_random=get_random_string(length=14)
    print(request.session)
    if "num" in request.session:
        request.session["num"]+=1
    else:
        request.session["num"]=0
    context={
        "var_aleatorio":var_random,
    }
    return render(request, "palabrasAleatorias.html", context)
def reset(request):
    request.session["num"]=0
    return index(request)