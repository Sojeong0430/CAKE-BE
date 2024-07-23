from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'name', 'birthday', 'email')
    
    username = forms.CharField(max_length=20, label="아이디")
    email = forms.EmailField(max_length=200)
    name = forms.CharField(max_length=20, label="이름")
    birthday = forms.DateField(label="생년월일", widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}))
    
    password1 = forms.CharField(label="비밀번호", widget=forms.PasswordInput)
    password2 = forms.CharField(label="비밀번호 확인", widget=forms.PasswordInput)

    def check_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
            raise forms.ValidationError("이미 사용 중인 사용자명입니다.")
        except User.DoesNotExist:
            return username