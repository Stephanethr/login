from django.db import models

class Objet(models.Model):
    TYPE_CHOICES = [
        ('potion', 'Potion'),
        ('plante', 'Plante'),
        ('arme', 'Arme'),
        ('cle', 'Clé'),
        ('armure', 'Pièce d\'armure'),
    ]

    nom = models.CharField(max_length=100)
    type_objet = models.CharField(max_length=10, choices=TYPE_CHOICES)
    quantite = models.PositiveIntegerField(default=1)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nom} ({self.type_objet})"
