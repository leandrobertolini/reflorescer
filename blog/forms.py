
from django.forms import SelectMultiple
from django import forms
from .models import Componentes


class PostForm(forms.ModelForm):

    class Meta:
        model = Componentes
        exclude = ('responsavel',)

        widgets = {
            'pagamento': SelectMultiple(attrs={'class': 'full-width'}),
        }
