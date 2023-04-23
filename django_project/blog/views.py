from django.shortcuts import render
from .models import Post
import feedparser
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    """
        Feeds which are to be displayed are extracted from techcrunch.
        A separate Post model is created where the blogs are stored in DB.
        
        - Currently we can add the data in Post from admin page. Functionality for adding 
          blog from  UI needs to be added.
    """
    feeds = feedparser.parse('https://techcrunch.com/feed/')
    context = {
        'posts': Post.objects.all(),
        'feeds' : feeds
    }

    return render(request, 'blog/home.html', context)

@login_required
def about(request):
    """
        Renders about page template when this api is called
    """
    return render(request, 'blog/about.html', {'title': 'About'})