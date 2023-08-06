from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    size = forms.ChoiceField(choices=(('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')), widget=forms.Select(attrs={'class': 'form-control', 'redaonly': 'readonly'}))
    