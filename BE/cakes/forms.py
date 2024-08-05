from django import forms
from .models import message

class MessageForm(forms.ModelForm):
    class Meta:
        model = message
        fields = ['message_content']
        labels={
            'message_content' : '내용'
        }