from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser

class SignUpForm(UserCreationForm):
    password2 = forms.PasswordInput()

    class Meta:
        model = CustomUser 
        fields = ('email', 'username', 'password1', 'password2', 'full_name', 'contact_number' )
    
    def save(self, **kwargs):
        
        password = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError({'password': 'passwords does not match'})
        
        new_user = CustomUser.objects.create_user(username=self.cleaned_data['username'],
                            email=self.cleaned_data['email'],
                            full_name=self.cleaned_data['full_name'], 
                            contact_number=self.cleaned_data['contact_number'],
                            password=password)

        return new_user