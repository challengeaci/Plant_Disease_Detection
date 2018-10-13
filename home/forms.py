from django import forms

class UploadForm(forms.Form):
    CHOICES = (('0','Fruits'), ('1','Diseases'),)
    mode = forms.ChoiceField(widget=forms.Select, choices=CHOICES,label="")
    image=forms.ImageField(label='',)

