from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404

from django.http import HttpResponseRedirect
from django.urls import reverse


def change_status(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in ['draft', 'published']:  # Ensure the status is valid
            post.status = new_status
            post.save()
    return redirect('post_list')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})



def post_list(request):
    posts = Post.objects.filter(status='published').order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    liked = request.user in post.likes.all() if request.user.is_authenticated else False
    return render(request, 'blog/post_detail.html', {'post': post, 'liked': liked})
#def post_detail(request, pk):
#    post = get_object_or_404(Post, pk=pk)
#    return render(request, 'blog/post_detail.html', {'post': post})



#def post_like(request, pk):
#    post = get_object_or_404(Post, pk=pk)
#    if post.likes.filter(id=request.user.id).exists():
#        post.likes.remove(request.user)
#    else:
#        post.likes.add(request.user)
#    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))



def post_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user.is_authenticated:
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
    return redirect('post_detail', pk=pk)

def publish_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.status = 'published'
    post.save()
    return redirect('post_detail', pk=pk)