from django.shortcuts import render , get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth import get_user_model
from datetime import date
from .forms import MessageForm

@login_required
def myroom_own (request,user_id): 
    User = get_user_model()
    owner = User.objects.get(id=user_id)
    birthday = owner.birthday

    if birthday != date.today() :
        today = date.today()
        this_year_birthday = birthday.replace(year=today.year)

        if this_year_birthday < today:
            next_year_birthday = birthday.replace(year=today.year+1)
            d_day = (next_year_birthday - today).days
        else:
            d_day = (this_year_birthday - today).days
        
        birthday = birthday.strftime('%m월 %d일')

        context={
            'owner':owner, 
            'birthday':birthday,
            'd_day':d_day,
            }
        return render (request,'myroom/room_own.html',context)
    
    else:
        context={
        'owner':owner, 
        'birthday':birthday,
        }
    return render (request,'myroom/room_own_Dday.html',context)

def myroom_visitor (request,user_id):
    User = get_user_model()
    owner = User.objects.get(id=user_id)
    birthday = owner.birthday

    if birthday != date.today() :
        today = date.today()
        this_year_birthday = birthday.replace(year=today.year)

        if this_year_birthday < today:
            next_year_birthday = birthday.replace(year=today.year+1)
            d_day = (next_year_birthday - today).days
        else:
            d_day = (this_year_birthday - today).days
        
        birthday = birthday.strftime('%m월 %d일')

        context={
            'owner':owner, 
            'birthday':birthday,
            'd_day':d_day,
            }
        return render (request,'myroom/room_visitor.html',context)
    
    else:
        context={
        'owner':owner, 
        'birthday':birthday,
        }
    return render (request,'myroom/room_visitor_Dday.html',context)

def cake_custom (request,user_id):
    User = get_user_model()
    owner = User.objects.get(id=user_id)
    context = {
        'owner' : owner
    }
    return render (request,'myroom/cakemaker.html',context)

def message_open (request,user_id):
    User = get_user_model()
    owner = User.objects.get(id=user_id)
    context = {
        'owner' : owner
    }
    return render(request,'myroom/message_open.html',context)

def create_message (request,user_id):
    User = get_user_model()
    owner = User.objects.get(id=user_id)
    form = MessageForm()
    context = {'form':form,
               'owner':owner}
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.party = owner
            message.save()
            return redirect('cakes:visitor',user_id=owner.id)
    else: 
        return render(request,'myroom/messagemaker.html',context)