from django.forms import ModelForm, Textarea
from .models import Poem

class PoemForm(ModelForm):
    class Meta:
        model = Poem
        fields = ['author', 'title', 'text']
        widgets = {
            'text': Textarea(),
        }