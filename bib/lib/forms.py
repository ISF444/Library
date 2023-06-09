from django import forms

from .models import BookRegis, RegisNewReaders


class FormBookRegis(forms.ModelForm):
    class Meta:
        model = BookRegis
        fields = '__all__'


class FormRegisNewReaders(forms.ModelForm):
    data_of_birth = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '01.01.2001'}))

    class Meta:
        model = RegisNewReaders
        fields = '__all__'
