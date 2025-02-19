from django import forms
from django.core.exceptions import ValidationError
from . import models


class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Введите почту'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имя'}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите фамилию'}))
    avatar = forms.ImageField()
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))
    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if models.User.objects.filter(username=username).exists():
            raise ValidationError('Такое имя пользователя уже занято')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if models.User.objects.filter(email=email).exists():
            raise ValidationError('Такой адрес электронной почты уже занят')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password_confirmation')
        if password and password_confirmation and password != password_confirmation:
            raise ValidationError('Пароли не совпадают')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    class Meta:
        model = models.User
        fields = ['username', 'email', 'name', 'surname', 'avatar']


class LoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))

    class Meta:
        model = models.User
        fields = ['password']
