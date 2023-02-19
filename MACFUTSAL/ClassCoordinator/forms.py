
from django import forms
from .models import Team_Registration


class AddForm(forms.ModelForm):

    class Meta:
        model = Team_Registration
        fields = ('Team_Name', 'Team_Manager', 'Goal-Keeper','Striker-1', 'Striker-2','Defeander-1','Defeander-2','Subs-1','Subs-2','Subs-3','Subs-4' )

        widgets = {
            'Team_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Team_Manager': forms.TextInput(attrs={'class': 'form-control'}),
            'Goal_Keeper': forms.TextInput(attrs={'class': 'form-control'}),
            'Striker_1': forms.TextInput(attrs={'class': 'form-control'}),
            'Striker_2': forms.TextInput(attrs={'class': 'form-control'}),
            'Defeander_1': forms.TextInput(attrs={'class': 'form-control'}),
            'Defeander_2': forms.TextInput(attrs={'class': 'form-control'}),
            'Subs_1': forms.TextInput(attrs={'class': 'form-control'}),
            'Subs_2': forms.TextInput(attrs={'class': 'form-control'}),
            'Subs_3': forms.TextInput(attrs={'class': 'form-control'}),
            'Subs_4': forms.TextInput(attrs={'class': 'form-control'}),
        }
