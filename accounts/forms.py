from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    
    role = forms.CharField(max_length=30, required=False, help_text='Optional.')
    #organisation = forms.CharField(max_length=30, required=False, help_text='Optional.')
    house_name_no = forms.CharField(max_length=30, required=False, help_text='Optional.')
    street = forms.CharField(max_length=30, required=False, help_text='Optional.')
    town = forms.CharField(max_length=30, required=False, help_text='Optional.')
    county = forms.CharField(max_length=30, required=False, help_text='Optional.')
    postcode = forms.CharField(max_length=30, required=False, help_text='Optional.')
    tel = forms.CharField(max_length=30, required=False, help_text='Optional.')
    #gdpr_consent = forms.CharField(max_length=30, required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',
                  'role',
                  #'organisation',
                  'house_name_no',
                  'street',
                  'town',
                  'county',
                  'postcode',
                  'tel',
                  #'gdpr_consent',
                  )
