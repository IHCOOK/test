from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('type', 'name', 'author', 'grade', 'memo')
        widgets = {
            'type': forms.RadioSelect(),
            'name': forms.TextInput(attrs={'placeholder': '記入例：姑獲鳥の夏'}),
            'author': forms.TextInput(attrs={'placeholder': '記入例：京極 夏彦'}),
            'grade': forms.RadioSelect(),
            'memo': forms.Textarea(attrs={'rows': 4}),
        }
