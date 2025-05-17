from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    ROLE_CHOICES = [
        ('user', 'Покупатель'),
        ('store_owner', 'Владелец магазина'),
    ]

    role = forms.ChoiceField(choices=ROLE_CHOICES, label='Тип пользователя')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'role']
        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }
        labels = {
            'username': 'Имя пользователя',
            'email': 'Электронная почта',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'password1': 'Пароль',
            'password2': 'Подтверждение пароля',
        }
        help_texts = {
            'username': 'Введите уникальное имя пользователя.',
            'email': 'Введите действующий адрес электронной почты.',
            'first_name': 'Введите ваше имя.',
            'last_name': 'Введите вашу фамилию.',
            'password1': 'Введите пароль.',
            'password2': 'Подтвердите пароль.',
        }
        error_messages = {
            'username': {
                'required': 'Это поле обязательно для заполнения.',
                'unique': 'Это имя пользователя уже занято.',
            },
            'email': {
                'required': 'Это поле обязательно для заполнения.',
                'invalid': 'Введите действительный адрес электронной почты.',
            },
            'password1': {
                'required': 'Это поле обязательно для заполнения.',
                'too_common': 'Пароль слишком распространен.',
                'too_short': 'Пароль слишком короткий. Минимум 8 символов.',
            },
            'password2': {
                'required': 'Это поле обязательно для заполнения.',
                'mismatch': 'Пароли не совпадают.',
            },
        }