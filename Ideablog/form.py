from django import forms

class AmountForm(forms.Form):
    Amount = forms.IntegerField(
        
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": " Enter the amount you want to donate eg 5"
        })
    )