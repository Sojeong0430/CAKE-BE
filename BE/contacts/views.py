from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # 기본값으로 Contact 객체 생성
            contact = Contact(
                name='이름 없음',
                birthday='2000-01-01',
                d_day='2000-01-01',
                party_room_address=form.cleaned_data['party_room_address']
            )
            contact.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'contacts/add_contact.html', {'form': form})


