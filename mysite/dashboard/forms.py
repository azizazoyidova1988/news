from django import forms
from .models import *


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        labels={
            "name":"Enter name"
        }

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"
        labels={
            "name":"Enter name"
        }

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"
        labels={
            "name":"Enter name"
        }


class ReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = "__all__"
        labels={
            "name":"Enter name"
        }