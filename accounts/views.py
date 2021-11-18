from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import time
from Topic.models import UserProfile
from Topic.forms import ProfileForm, UserForm
# Create your views here.

#---------------------------View for Log In-------------------------------------------------

def logIn(request):
    if request.method == 'POST':
        uName = request.POST['uname']
        password = request.POST['password']
        user = auth.authenticate(username=uName, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.info(request, 'You Are Loged In As ' + uName)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password!')
            return redirect('accounts:logIn')
        
    else:
        return render(request, 'accounts/logIn.html')

#---------------------------View for Log Out-------------------------------------------------

def logOut(request):
    auth.logout(request)
    return redirect('home')

#---------------------------View for Sign Up-------------------------------------------------

def signUp(request):
    if request.method == 'POST':
        fName = request.POST['fname']
        lName = request.POST['lname']
        email = request.POST['email']
        uName = request.POST['uname']
        pass1 = request.POST['passw']
        pass2 = request.POST['cpassw']
        
        if pass1 == pass2:
            if User.objects.filter(username=uName).exists():
                messages.info(request, 'Username already exists!')
                return redirect('accounts:signUp')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists!')
                return redirect('accounts:signUp')
            elif (uName == pass1) or (uName in pass1):
                messages.info(request, 'Username and Password can not be same!')
                return redirect('accounts:signUp')
            else:
                user = User.objects.create_user(first_name=fName, last_name=lName, username=uName, email=email, password=pass1)
                user.save()
                user_profile = UserProfile.objects.create(user=user)
                user_profile.save()
                messages.info(request, 'Account created successfully!')
                time.sleep(3)
                return redirect('accounts:logIn')
        else:
            messages.info(request, 'Password does not match!')
            return redirect('accounts:signUp')
    else:
        return render(request, 'accounts/signUp.html')
    
#---------------------------View for Forgot Password-------------------------------------------------        
    
def forgot(request):
    if request.method == 'POST':
        email = request.POST['email']
        pasw = request.POST['password']
        
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            user.set_password(pasw)
            user.save()
            messages.info(request, 'Password Changed Successfully!')
            return redirect('accounts:logIn')
        else:
            messages.info(request, 'Email not registered!')
            return redirect('accounts:forgot')
    else:
        return render(request, 'accounts/forgot.html')
    
#---------------------------View for Profile-------------------------------------------------    

def profile(request):
    if request.user.is_authenticated:
        topics = request.user.topic_set.count()
        context = {'topics': topics}
        return render(request, 'accounts/profile.html', context)
    else:
        return redirect('/logIn')


#---------------------------View for Edit Profile------------------------------------------------- 

def edit_profile(request):
    if request.method != 'POST':
        form = UserForm(instance=request.user)
        if request.user.userprofile:
            p_form = ProfileForm(instance=request.user.userprofile)
        else:
            messages.info(request, 'User has no User Profile!')
            return render(request, 'accounts/profile.html')
    else:
        form = UserForm(instance=request.user, data=request.POST)
        p_form = ProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid() and p_form.is_valid():
            form.save()
            p_form.save()
            return redirect('accounts:profile')
        
    context = {'form': form, 'p_form': p_form}
    return render(request, 'accounts/edit_profile.html', context)