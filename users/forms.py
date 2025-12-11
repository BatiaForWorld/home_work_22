from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import User
import re


class UserRegisterForm(UserCreationForm):
    usable_password = None

    class Meta:
        model = User
        fields = [
            "email",
            "password1",
            "password2",
            "avatar",
            "phone",
            "country",
        ]

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and not re.match(r'^\+?\d{7,15}$', phone):
            raise forms.ValidationError("Введите корректный номер телефона, например +71234567890")
        return phone

    def clean_country(self):
        country = self.cleaned_data.get('country')

        if country:
            if len(country) < 2:
                raise forms.ValidationError("Название должно быть не короче 2 символов.")

            if not re.match(r'^[A-Za-zА-Яа-яЁё\s-]+$', country):
                raise forms.ValidationError("Название должно содержать только буквы, пробелы и дефис.")

        return country

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email:
            forbidden_domains = ["mailinator.com", "10minutemail.com"]
            domain = email.split("@")[-1]

            if domain in forbidden_domains:
                raise forms.ValidationError("Использование временных email запрещено.")

        return email

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')

        if avatar and avatar.size > 2 * 1024 * 1024:
            raise forms.ValidationError("Размер аватара не может превышать 2MB.")

        return avatar

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

        self.fields['email'].widget.attrs.update({
            'placeholder': 'Введите ваш email'
        })
        self.fields['avatar'].widget.attrs.update({
            'placeholder': 'Добавьте ваш аватар'
        })
        self.fields['country'].widget.attrs.update({
            'placeholder': 'Укажите город или страну'
        })
        self.fields['phone'].widget.attrs.update({
            'placeholder': 'Введите ваш номер телефона'
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Пароль не менее 8 символов'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Повторите пароль'
        })


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите ваш email'
        })

        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите пароль'
        })
