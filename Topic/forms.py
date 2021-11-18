from django import forms
from .models import Topic, Entry, UserProfile
from django.contrib.auth.models import User 
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'image']
        labels = {'title': 'Topic Name', 'image': 'Topic Image'}
        
        


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'image']
        labels = {'bio': 'Bio', 'image': 'Profile Picture'}
        

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'username': 'Username', 'email': 'Email'} 
 
           