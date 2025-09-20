"""
File: views.py
Author: Reagan Zierke <reaganzierke@gmail.com>
Date: 2025-09-20
Description: Views for forum interactions, including message posting and threading.
"""



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message
from posts.models import Post
from .forms import MessageForm

@login_required(login_url="/account/login/")
def thread_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    messages = Message.objects.filter(parent=None, post=post).order_by('-timestamp')
    form = MessageForm(request.POST or None)
    parent_id = request.POST.get('parent_id')
    parent = Message.objects.filter(id=parent_id).first() if parent_id else None

    if request.method == 'POST' and form.is_valid():
        msg = form.save(commit=False)
        msg.author = request.user
        msg.parent = parent
        msg.post = post
        msg.save()
        return redirect('thread_view', slug=slug)

    return render(request, 'forum/thread.html', {
        'post': post,
        'messages': messages,
        'form': form,
        'parent_id': parent_id,
    })

def get_replies(message):
    return message.replies.all().order_by('timestamp')

# Existing delete_message view
@login_required(login_url="/account/login/")
def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id, author=request.user)
    message.delete()
    return redirect('/')
