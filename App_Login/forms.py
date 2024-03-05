from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, UserProfile

class StudentRegistrationForm(UserCreationForm):
    student_field = forms.CharField(max_length=100, required=False, help_text='Additional field for students')
    email = forms.EmailField(label="Email Address", required=True)
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'student_field', 'profile_picture']
        labels = {
            'username': 'Username',
            'password1': 'Password',
            'password2': 'Confirm Password',
            'student_field': 'Student Field',
            'profile_picture': 'Profile Picture',
        }

class TeacherRegistrationForm(UserCreationForm):
    teacher_field = forms.CharField(max_length=100, required=False, help_text='Additional field for teachers')
    email = forms.EmailField(label="Email Address", required=True)
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'teacher_field', 'profile_picture']
        labels = {
            'username': 'Username',
            'password1': 'Password',
            'password2': 'Confirm Password',
            'teacher_field': 'Teacher Field',
            'profile_picture': 'Profile Picture',
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password1', 'password2', 'profile_picture']