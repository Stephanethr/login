from django import forms
from .models import Objet

class ObjetForm(forms.ModelForm):
    class Meta:
        model = Objet
        fields = ['nom', 'type_objet', 'quantite', 'description']
