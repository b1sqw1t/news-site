from django                         import forms
from .models import Blog_model


class Blog_forms(forms.ModelForm):
    class Meta:
        model = Blog_model
        fields = 'Title', 'Author', 'Text'


