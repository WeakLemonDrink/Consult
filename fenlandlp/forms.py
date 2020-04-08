from .models import Comment
from django.contrib.auth.models import User
from accounts.models import Client
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'client',
            'body',
            'file',
            ]
        exclude = ['user']
        
    def __init__(self, user, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['client'].queryset = Client.objects.filter(agent__username=user)
 
