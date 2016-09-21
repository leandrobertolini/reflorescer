
from django.forms import SelectMultiple
from django import forms
from .models.componente import Componente


class PostForm(forms.ModelForm):

    class Meta:
        model = Componente
        exclude = ('responsavel',)

        widgets = {
            'pagamento': SelectMultiple(attrs={'class': 'full-width'}),
        }
