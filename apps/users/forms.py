from django import forms


class LoginForm(forms.Form):
    login = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Логин...',
                'class': 'form-control',
                'id': 'exampleInputLogin'
            }
        )
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Пароль...',
                'class': 'form-control',
                'id': 'exampleInputPassword'
            }
        ),
    )
