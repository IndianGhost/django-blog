#-*- coding: utf-8 -*-
from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

# Create your views here.
def home(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    text = """<h1>Bienvenue sur mon blog !</h1>
              <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""
    return HttpResponse(text)

def date_actuelle(request):
    vue         =   "blog/date.html"
    attribut    =   {'today' : datetime.now()}
    return render(request, vue, attribut)

def addition(request, nombre1, nombre2):
    vue         =   "blog/addition.html"
    nombre1     =   int(nombre1)
    nombre2     =   int(nombre2)
    attribut    =   {
        'x': nombre1,
        'y': nombre2,
        'somme' : (nombre1+nombre2)
    }
    return render(request, vue, attribut)

def inscription_form(request):
    vue = 'blog/inscription.html'
    return render(request, vue)

def inscription(request):
    vue = 'blog/inscription.html'
    attribut = locals()
    if request.method=='GET':
        titre   =   request.GET['titre']
        auteur  =   request.GET['auteur']
        contenu =   request.GET['contenu']
    return render(request, vue, attribut)

def article(request, id):
    vue         =   'blog/article.html'
    attribut    =   {'id': id}
    #ternary operator assignment
    #Syntax : value_in_true_case if condition else value_in_false_case
    return render(request, vue) if (id is None) else render(request, vue, attribut)