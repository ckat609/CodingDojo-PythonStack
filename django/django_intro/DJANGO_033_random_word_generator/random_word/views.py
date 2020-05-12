from django.shortcuts import render, redirect
import random

# Create your views here.


def index(request):
    return redirect("/random_word")


def reset(request):
    del request.session['count']

    return redirect("/random_word")


def random_word(request):
    if 'count' not in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1

    randomWord = ""
    for i in range(15):
        aNum = random.randint(48, 122)
        if (aNum >= 91 and aNum <= 96) or (aNum >= 58 and aNum <= 64):
            i -= 1
        else:
            # aChar = chr(aNum)
            randomWord += chr(aNum)
            print(aNum)
    request.session['randomWord'] = randomWord

    return render(request, "index.html")
