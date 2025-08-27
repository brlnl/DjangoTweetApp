from django import forms
from tweetapp.models import Tweet
from django.forms import ModelForm

class AddTweetForm(forms.Form):
    nickname_input = forms.CharField(label='Nickname', max_length=100)
    message_input = forms.CharField(label='Message', max_length=280, widget=forms.Textarea())

class AddTweetModelForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ['nickname', 'message']