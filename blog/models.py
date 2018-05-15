from django.db import models
from django.utils import timezone
# Create your models here.
class Article(models.Model):
    titre       =   models.CharField(max_length=100)
    auteur      =   models.CharField(max_length=42)
    contenu     =   models.TextField(null=True)
    date        =   models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    categorie   =   models.ForeignKey('Categorie')

    def __unicode__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard et dans l'administration
        """
        return self.titre

class Categorie(models.Model):
    """docstring for Categorie"""
    nom = models.CharField(max_length=30)
    def __init__(self):
        return self.nom
        