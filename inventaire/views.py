from django.shortcuts import render, get_object_or_404, redirect
from .models import Objet
from .forms import ObjetForm

# Lister les objets de l'inventaire
def objet_list(request):
    objets = Objet.objects.all()
    return render(request, 'inventaire/objet_list.html', {'objets': objets})

# Ajouter un nouvel objet
def objet_create(request):
    if request.method == 'POST':
        form = ObjetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('objet_list')
    else:
        form = ObjetForm()
    return render(request, 'inventaire/objet_form.html', {'form': form})

# Modifier un objet existant
def objet_update(request, pk):
    objet = get_object_or_404(Objet, pk=pk)
    if request.method == 'POST':
        form = ObjetForm(request.POST, instance=objet)
        if form.is_valid():
            form.save()
            return redirect('objet_list')
    else:
        form = ObjetForm(instance=objet)
    return render(request, 'inventaire/objet_form.html', {'form': form})

# Supprimer un objet
def objet_delete(request, pk):
    objet = get_object_or_404(Objet, pk=pk)
    if request.method == 'POST':
        objet.delete()
        return redirect('objet_list')
    return render(request, 'inventaire/objet_confirm_delete.html', {'objet': objet})
