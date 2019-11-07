from django.shortcuts import render, redirect

from django.contrib.auth.decorators import user_passes_test

from .models import Cooperatives
from .forms import CooperativesForm, CooperativesUpdateForm


def list_cooperatives(request):
    cooperatives = Cooperatives.objects.all()
    return render(request, 'cooperatives.html', {'cooperatives': cooperatives})


@user_passes_test(lambda u: u.is_superuser)
def create_cooperative(request):
    form = CooperativesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_cooperatives')
    return render(request, 'cooperative-form.html', {'form': form})


def update_cooperative(request, coop_name):
    cooperative = Cooperatives.objects.get(coop_name=coop_name)
    form = CooperativesUpdateForm(request.POST or None, instance=cooperative)
    if form.is_valid():
        form.save()
        return redirect('list_cooperatives')
    return render(request, 'cooperative-form.html', {'form': form, 'cooperative': cooperative})


def delete_cooperative(request, coop_name):
    cooperative = Cooperatives.objects.get(coop_name=coop_name)
    if request.method == 'POST':
        cooperative.delete()
        return redirect('list_cooperatives')
    return render(request, 'cooperative-delete-confirm.html', {'cooperative': cooperative})
