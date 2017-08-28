from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            "restaurant",
            "name",
            "contents",
            "public",
            "excludes"
        ]
    def __init__(self,user = None, *args, **kwargs):
        print(user)
        super(ItemForm, self).__init__(*args, **kwargs)

