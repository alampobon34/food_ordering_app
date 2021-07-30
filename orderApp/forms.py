from typing import Text
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Hidden, Layout, Row, Column, Submit
from crispy_forms.bootstrap import InlineField, PrependedText
from django import forms
from django.forms.fields import ChoiceField
from django.forms.widgets import TextInput
from django.http import request
from orderApp.models import *
from django.forms import ModelForm, TextInput, NumberInput, EmailInput, PasswordInput, Select, FileInput,DateInput,DateField,ChoiceField, widgets




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


class ShippingAddressForm(forms.ModelForm):

    class Meta:
        model = ShippingAddress
        fields = ['customer','order','address','area','houseNo','zipcode']

    widgets = {
        'customer': forms.HiddenInput(),
        'order':forms.HiddenInput(),
        'address': TextInput(attrs={'class': 'form-control', 'placeholder': 'birth_date','type':'textarea'}),
        'area': Select(attrs={'class':'form-control form-select', 'placeholder': 'select a option','aria-label': 'Default select example'}, choices=CITY),
        'houseNo': TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your house no.','type':'text'}),
        'zipcode': TextInput(attrs={'class': 'form-control','type':'text'})
    }
    
    def __init__(self, *args, **kwargs):
        super(ShippingAddressForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.initial['customer'] = request.user.profile