from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('responsavel','nome','cidade','telefone','email','manequim','calcado','pagamento','obs',)