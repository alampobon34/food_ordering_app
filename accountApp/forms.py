from typing import Text
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from crispy_forms.bootstrap import InlineField, PrependedText
from django import forms
from django.forms.fields import ChoiceField
from django.http import request
from accountApp.models import *
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,UserChangeForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, NumberInput, EmailInput, PasswordInput, Select, FileInput,DateInput,DateField,ChoiceField, widgets


class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Email Address','type':'email','id':'email'}),
        required=True,
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username','type':'text','id':'username'}),
        required=True
    )
    password1 = forms.CharField(
        widget= forms.PasswordInput(attrs={'placeholder': '***********','type':'password','id':'password1'}),
        required=True
    )
    password2 = forms.CharField(
        widget= forms.PasswordInput(attrs={'placeholder': '***********','type':'password','id':'password2'}),
        required=True
    )
	
    class Meta:
        model=User
        fields=['username','email','password1','password2']

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["username"].label = ""
        self.fields["password1"].label = ""
        self.fields["email"].label = ""
        self.fields["password2"].label = ""


    
    def clean_password(self, *args, **kwargs):
        password = self.cleaned_data['password1']
        cpassword = self.cleaned_data['password2']
        if len(password)<8:
            raise forms.ValidationError("Password is too short...")
        elif password == None:
            raise forms.ValidationError("Password field can not be empty..")
        elif (password!=cpassword):
            raise forms.ValidationError("Password field does not match..")



class LoginForm(forms.Form):
    email=forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Email Address',
        'type':'email',
        'id':'login_email',
        'class':'form-control'}),
        required=True,
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '***********','type':'password',
        'id':'login_password',
        'class':'form-control'}),
        required=True

    )

    class Meta:
        model = User
        fields = ['email', 'password',]

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    def clean_password(self, *args, **kwargs):
        password = self.cleaned_data['password']
        if len(password)<8:
            raise forms.ValidationError("Password is too short...")
        elif password == None:
            raise forms.ValidationError("Password field can not be empty..")


    


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control','type':'password',
        'placeholder': '***********',
        'id':'old_password'
        }),
        required=True
    )

    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control','type':'password',
        'placeholder': '***********',
        'id':'new_password1'
        }),
        required=True
    )

    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control','type':'password',
        'placeholder': '***********',
        'id':'new_password2'
        }),
        required=True
    )

    class Meta:
        model=User
        fields=['old_password','new_password1','new_password2']

    def __init__(self, *args, **kwargs):
        super(PasswordChangingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["old_password"].label = ""
        self.fields["new_password1"].label = ""
        self.fields["new_password2"].label = ""



class UserUpdateForm(UserChangeForm):
    
    first_name =forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'first_name',
        'type':'text',
        'id':'first_name',
        'class':'form-control'}),
        required=False,
    )
    last_name=forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'last_name',
        'type':'text',
        'id':'last_name',
        'class':'form-control'}),
        required=False,
    )
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
        exclude = ['password','username','email']

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birthDate', 'gender', 'phone', 'image']

        widgets = {
            'birthDate': DateInput(attrs={'class': 'form-control', 'placeholder': 'birth_date','type':'date'}),
            'gender': Select(attrs={'class': 'form-control form-select', 'placeholder': 'gender'}, choices=GENDER_CHOICES),
            'phone': NumberInput(attrs={'class': 'form-control', 'placeholder': 'enter a phone number(016xxxxx)','type':'tel','pattern':'[+]{1}[8]{1}[8]{1}[0]{1}[0-9]{10}', 'value':'+880',}),
            'image': FileInput(attrs={'class': 'form-control','type':'file'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.fields["image"].label = ""



CITY = [
    ('Dhaka', 'Dhaka'),
    ('Mymensign', 'Mymensign'),
    ('Rajshahi', 'Rajshahi'),
    ('Rangpur', 'Rangpur'),
    ('Barisal', 'Barisal'),
    ('Chottogram', 'Chottogram'),
    ('Khulna', 'Khulna'),
    ('Comilla', 'Comilla'),
]


class AddressUpdateForm(forms.ModelForm):
    #address_type = forms.TextInput()
    # address = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control'}))
    # houseNo = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Address
        fields = ['address','area','houseNo','roadNo','zipCode']

    widgets = {
        'address': TextInput(attrs={'class': 'form-control', 'placeholder': 'Address','type':'textarea'}),
        'area': Select(attrs={'class':'form-control form-select', 'placeholder': 'gender','aria-label': 'Default select example'}, choices=CITY),
        'houseNo': TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your house no.','type':'text'}),
        'roadNo': TextInput(attrs={'class': 'form-control','type':'text'}),
        'zipCode': TextInput(attrs={'class': 'form-control','type':'text'})
    }
    
    def __init__(self, *args, **kwargs):
        super(AddressUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False


        

