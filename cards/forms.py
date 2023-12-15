from django import forms

class CardCheckForm(forms.Form):
    card_id = forms.IntegerField(required=True)
    solved = forms.BooleanField(required=False)
    
    
class CardArchiveForm(forms.Form):
    card_id = forms.IntegerField(required=True)
    