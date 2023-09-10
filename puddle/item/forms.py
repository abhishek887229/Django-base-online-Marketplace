from django import forms

from .models import Item
INPUT_CLASS='w-full py-4 px-6 rounded-xl border border-double bg-gray-200'

class NewItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=('Category','name','description','price','image')

        widgets={
            'Category':forms.Select(attrs={
                'class':INPUT_CLASS
            }),
            'name':forms.TextInput(attrs={
                'class':INPUT_CLASS
            }),
            'description':forms.Textarea(attrs={
                'class':INPUT_CLASS
            }),
            'price':forms.TextInput(attrs={
                'class':INPUT_CLASS
            }),
            'image':forms.FileInput(attrs={
                'class':INPUT_CLASS
            })

        }        


class EditItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=('name','description','price','image','is_sold')

        widgets={
            'name':forms.TextInput(attrs={
                'class':INPUT_CLASS
            }),
            'description':forms.Textarea(attrs={
                'class':INPUT_CLASS
            }),
            'price':forms.TextInput(attrs={
                'class':INPUT_CLASS
            }),
            'image':forms.FileInput(attrs={
                'class':INPUT_CLASS
            }),
            'is_sold':forms.CheckboxInput(attrs={
            })

        }
