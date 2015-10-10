from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
   # postss = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.filter(title='yogurt')
    return render(request, 'blog/post_list.html', {'posts': posts})