from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'name', 'birthday', 'email')
    
    username = forms.CharField(max_length=20, label="아이디")
    email = forms.EmailField(max_length=200)
    name = forms.CharField(max_length=20, label="이름")
    birthday = forms.DateField(
        label="생일",
        widget=forms.DateInput(format='%y-%m-%d', attrs={'type': 'date'})
        )
    
    password1 = forms.CharField(label="비밀번호", widget=forms.PasswordInput)
    password2 = forms.CharField(label="비밀번호 확인", widget=forms.PasswordInput)

    def check_username(self):
        username = self.cleaned_data['username']
        try:
            CustomUser.objects.get(username=username)
            raise forms.ValidationError("이미 사용 중인 사용자명입니다.")
        except CustomUser.DoesNotExist:
            return username
        
    def get_birthday(self):
        return self.birthday.strftime('%y-%m-%d') if self.birthday else ''