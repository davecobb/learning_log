from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import Topic
from .forms import TopicForm, EntryForm

def index(request):
    """The index of the Learning log"""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Show all topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics, 'dave': 'cobb'}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def topic_by_slug(request, slug):
    print(slug)
    topic = Topic.objects.get(slug=slug)
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Add New topic"""
    if request.method != "POST":
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Add New entry"""
    topic = Topic.objects.get(id=topic_id)

    #print(Topic.objects.get(id=topic_id).values())
    print("topic_id:")
    print(topic_id)
    print("reverse:")
    print(reverse('learning_logs:topic', args=[topic_id]))

    if request.method != "POST":
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            #print(new_entry.topic)
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def get_category1(request, subcategory, category):
    print(category)
    print(subcategory)

    #return HttpResponse("return this string")
    return render(request, 'learning_logs/test.html')

@login_required
def get_category2(request, subcategory, category):
    print(category)
    print(subcategory)

    context = {'category': category, 'subcategory': subcategory}

    #return HttpResponse("return this string")
    return render(request, 'learning_logs/test.html', context)
