from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100,required=False, 
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,required=False,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password1 = forms.CharField(max_length=50,required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']




class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


from django import forms

from django.contrib.auth.models import User
from .models import profile


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    MY_CHOICES = [
        ('', '---Please select an option---'),
        ('SV Mess', 'Vyas Bhawan'),
        ('BGVK Mess', 'Vishwakarma Bhawan'),
        ('KG Mess', 'Gandhi Bhavan'),
        ('KG Mess', 'Krishna Bhavan'),
        ('RMBD Mess', 'Budh Bhavan'),
        ('MR Mess', 'Meera Bhavan'),
        ('ML Mess', 'Malviya Bhavan'),
        ('BGVK Mess', 'Bhagirath Bhavan'),
        ('SV Mess', 'Shankar Bhavan'),
        ('RMBD Mess', 'Ram Bhavan'),
        ('SR Mess', 'SR Bhavan'),
        ('RPS Mess', 'Ashok Bhavan'),
        ('RPS Mess', 'Rana Pratap Bhavan') ]
    bits_id = forms.CharField(max_length=15,required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    mess = forms.ChoiceField(choices=MY_CHOICES,widget=forms.Select,required=True,initial='')
    class Meta:
        model = profile
        fields = ['bits_id', 'mess']
    
    

    # input_string = forms.ChoiceField(choices=MY_CHOICES)


from .models import Feedback

class FeedbackForm(forms.ModelForm):
    title=forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control','cols':10}))
    description=forms.Textarea( attrs={'class': 'form-control','rows': 5,'cols': 120})
    image = forms.ImageField(required=False, widget=forms.FileInput)

    class Meta:
        model = Feedback
        fields = ['title', 'description', 'image']

from .models import breakfast,lunch,dinner
class BKrating(forms.ModelForm):
    rating_choices = [
    (1, '1 star'),
    (2, '2 stars'),
    (3, '3 stars'),
    (4, '4 stars'),
    (5, '5 stars'),
]
    stars = forms.ChoiceField(required=False, label='Enter your rating', choices=rating_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = breakfast
        fields = ['stars']

from .models import attend
class BKattendance(forms.ModelForm):
    BKattend = forms.BooleanField(required=False)
   

class LHattendance(forms.ModelForm):
    has_attended_lunch = forms.BooleanField(required=False)
    
class DNattendance(forms.ModelForm):    
    has_attended_dinner = forms.BooleanField(required=False)
    