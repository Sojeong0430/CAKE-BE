from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['party_room_address']
        labels = {
            'party_room_address': '파티룸 주소',
        }

