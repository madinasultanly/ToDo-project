from django import forms

class ProfileForm(forms.Form):
    first_name = forms.CharField(label = 'Ad')
    last_name = forms.CharField(label = 'Soyad')
    email = forms.CharField(label = 'E-post')


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label="İstifadəçi adı")
    password = forms.CharField(max_length=20, label="Parol", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20, label="Parolu Doğrula", widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')

        if password and confirm and password != confirm:
            raise forms.ValidationError("Parollar Eyni Deyil!")

        values = {
            "username": username,
            "password": password,
            
        }
        return values


class LoginForm(forms.Form):
    username = forms.CharField(label="İstifadəçi adı")
    password = forms.CharField(label="Parol", widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
    }))
    