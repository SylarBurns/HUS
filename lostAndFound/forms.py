from django.forms import ModelForm
from django.forms.widgets import Select

from heart.models import (
    Post
)

class lostAndFoundPostModelForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'boardType',
            'itemType',
        ]