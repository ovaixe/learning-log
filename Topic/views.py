from django.shortcuts import render, redirect
from .models import Topic, Entry, Subscribe
from .forms import TopicForm, EntryForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.

def checkUser(request, topic):
    # Checks if user requests for their own data
    if topic.user != request.user:
        raise Http404

#-----------------------------View for home---------------------------------------------------

def home(request):
    
    return render(request, 'topics/home.html')

#-----------------------------View for Topics---------------------------------------------------

@login_required
def topic(request):
    topics = request.user.topic_set.order_by('-date_added')
    context = {'topics': topics}
    
    
    return render(request, 'topics/topic.html', context)

#----------------------------View for Topic Entries----------------------------------------------------

def entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    # Check for user
    checkUser(request, topic)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    
    return render(request, 'topics/entry.html', context)
    
#---------------------------View for Adding New Topic-----------------------------------------------------    
    
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        # Display a blank or invalid form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(request.POST, request.FILES)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.user = request.user
            new_topic.save()    
            return redirect('topic')
        else:
            messages.info(request, 'Topic does not add')
            return redirect('home')
        
    context = {'form': form}
    return render(request, 'topics/new_topic.html', context)

#------------------------View for Adding New Entry--------------------------------------------------------

def addEntry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    # Check for user
    checkUser(request, topic)
    
    if request.method == 'POST':
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entrty = form.save(commit=False)
            new_entrty.topic = topic
            new_entrty.save()
            return redirect('topic')
    else:
        # No data submitted; create a blank form.
        # Display a blank or invalid form.
        form = EntryForm()
        
    context = {'topic': topic, 'form': form}
    return render(request, 'topics/addEntry.html', context)

#-----------------------View for Editing Entry---------------------------------------------------------

def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    # Check for user
    checkUser(request, topic)
    
    if request.method != 'POST':
        # No data submitted; create a blank form.
        # Display a blank or invalid form.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('topic')
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'topics/edit_entry.html', context)


#-----------------------View for Subscribe---------------------------------------------------------

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email', False)
        s_email = Subscribe.objects.create(email=email)
        s_email.save()
        return redirect('home')
    else:
        raise Http404
    

#-----------------------View for Delete Entry---------------------------------------------------------

def delete_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    entry.delete()
    return redirect('topic')

#-----------------------View for Delete Entry---------------------------------------------------------

def delete_topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    topic.delete()
    return redirect('topic')