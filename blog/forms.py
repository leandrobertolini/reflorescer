
from django.forms import SelectMultiple
from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ('responsavel',)

        widgets = {
            'pagamento': SelectMultiple(attrs={'class': 'full-width'}),
        }
