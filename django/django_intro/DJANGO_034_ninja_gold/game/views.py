from django.shortcuts import render, redirect
import random

# ******** NOT A VIEW


def switch_case(source):
    switcher = {
        'house': random.randint(2, 5),
        'farm': random.randint(10, 20),
        'cave': random.randint(5, 10),
        'casino': random.randint(-50, 50)
    }
    return switcher[source]


# ********* VIEWS

def index(request):
    return render(request, "index.html")


def landing_page(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []

    print(request.session['activitiesAmount'])
    print(request.session['gold'])
    return render(request, "index.html")


def process_gold(request, source=""):
    if request.method == 'POST':
        goldSource = request.POST['source']
        goldAmount = switch_case(request.POST['source'])
        print("POST")
        print(request.POST['source'])
        print("POST")
    else:
        goldSource = source
        goldAmount = switch_case(source)
        print("GET")
        print(source)
        print("GET")

    # print(request.POST['source'])
    request.session['gold'] += goldAmount

    if (goldAmount >= 0):
        activitiesContent = f"<p class='win'>{goldAmount} was earned from the {goldSource}</p>"
    else:
        activitiesContent = f"<p class='lost'>{abs(goldAmount)} was lost at the {goldSource}</p>"

    if(len(request.session['activities']) > 3):
        request.session['activities'] = request.session['activities'][:3]
    request.session['activities'].insert(0, activitiesContent)

    request.session['activitiesAmount'] = len(request.session['activities'])
    print(request.session['activitiesAmount'])
    return redirect("/")


def reset_all(request):
    del request.session['gold']
    del request.session['activities']
    return redirect("/")
