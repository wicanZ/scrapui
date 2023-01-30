from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from scrapui.models import ScrapItem

class RegistrationForm(UserCreationForm):
    #first_name = forms.CharField(max_length=101)
    #last_name = forms.CharField(max_length=101)
    username = forms.CharField(label='username',max_length=50 , widget=forms.TextInput(
        attrs={'class':'form-control'}
    ))
    email = forms.EmailField(label='Email',max_length=50 , widget=forms.TextInput(
        attrs={'class':'form-control'}
    ))
    password1 = forms.CharField(label='password',max_length=50 , widget=forms.PasswordInput(
        attrs={'class':'form-control'}
    ))
    password2 = forms.CharField(label='confirm password',max_length=50 , widget=forms.PasswordInput(
        attrs={'class':'form-control'}
    ))

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']

class Scrapform( forms.ModelForm ) :
    name = forms.CharField(label='title',max_length=50 , widget=forms.TextInput(
        attrs={'class':'form-control'}
    ))
    address = forms.CharField(label='address',max_length=50 , widget=forms.TextInput(
        attrs={'class':'form-control'}
    ))
    phone = forms.CharField(label='phone number',max_length=50 , widget=forms.TextInput(
        attrs={'class':'form-control'}
    ))
    # city = forms.CharField(label='city',max_length=50 , widget=forms.TextInput(
    #     attrs={'class':'form-control'}
    # ))
    # state = forms.CharField(label='state',max_length=50 , widget=forms.TextInput(
    #     attrs={'class':'form-control'}
    # ))
    zip = forms.IntegerField(label='zip' , widget=forms.NumberInput(
        attrs={'class':'form-control'}
    ))
    descriptive = forms.CharField(label='Descriptive',max_length=500 , widget=forms.Textarea(
        attrs={'class':'form-control','placeholder':' Please provide your question and any additional context that will be usefull for our team','rows':5}
    ))
    class Meta :
        model = ScrapItem
        fields = ['name','address','phone','zip','descriptive','images'] # 'city','state',
        exclude = ['user']

