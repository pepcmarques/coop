from django import forms
from .models import Cooperatives


class CooperativesForm(forms.ModelForm):
    class Meta:
        model = Cooperatives
        fields = ['coop_name']
        labels = {'coop_name': 'Cooperative name'}


class CooperativesUpdateForm(forms.ModelForm):
    class Meta:
        model = Cooperatives
        fields = ['coop_name', 'coop_address1', 'coop_address2', 'coop_city', 'coop_province', 'coop_country']
        labels = {
            'coop_name': 'Cooperative name',
            'coop_address1': 'Address',
            'coop_address2': 'completent',
            'coop_city': 'City',
            'coop_province': 'Province',
            'coop_country': 'Country'
        }
