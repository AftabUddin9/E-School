from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfile
from .forms import StudentRegistrationForm, TeacherRegistrationForm, UserProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            
            user.user_type = request.POST.get('user_type', 'student')

            if user.user_type == 'student':
                student_form = StudentRegistrationForm(request.POST)
                if student_form.is_valid():
                    user.save()
                    student_profile = student_form.save(commit=False)
                    student_profile.user = user
                    student_profile.save()
                    return HttpResponseRedirect(reverse('App_Login:login'))
            elif user.user_type == 'teacher':
                teacher_form = TeacherRegistrationForm(request.POST)
                if teacher_form.is_valid():
                    user.save()
                    teacher_profile = teacher_form.save(commit=False)
                    teacher_profile.user = user
                    teacher_profile.save()
                    return HttpResponseRedirect(reverse('App_Login:login'))
    else:
        form = UserCreationForm()

    return render(request, 'App_Login/register.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'App_Login/login.html', {'form': form})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Login:login'))


@login_required
def user_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'App_Login/user_profile.html', {'user_profile': user_profile})


@login_required
def edit_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=user_profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('user_profile')
        else:
            profile_form = UserProfileForm(request.POST, instance=user_profile)
        
        return render(request, 'edit_profile.html', {'profile_form': profile_form})