"""
File: views.py
Author: Reagan Zierke <reaganzierke@gmail.com>
Date: 2025-09-20
Description: Views for the main feed and post specific pages.
"""



from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from events.models import Event
from community_projects.models import CommunityProject
from creations.models import Creation
from posts.models import Post


@login_required
def home(request):
    events = Event.objects.all()
    projects = CommunityProject.objects.all()
    creations = Creation.objects.all()
    all_items = sorted(
        list(events) + list(projects) + list(creations),
        key=lambda item: item.created_at,
        reverse=True
    )
    
    return render(request, "feed/home.html", {
        "posts": all_items
    })


def view_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    # Get the actual subclass instance for correct template context
    if post.post_type == 'event':
        try:
            post_obj = post.event
        except Exception:
            post_obj = Event.objects.get(pk=post.pk)
        template = "events/view_event.html"
    elif post.post_type == 'community_project':
        try:
            post_obj = post.communityproject
        except Exception:
            post_obj = CommunityProject.objects.get(pk=post.pk)
        template = "community_projects/view_project.html"
    elif post.post_type == 'creation':
        try:
            post_obj = post.creation
        except Exception:
            post_obj = Creation.objects.get(pk=post.pk)
        template = "creations/view_creation.html"
    else:
        post_obj = post
        template = "feed/post_detail.html"

    # Forum message logic (for events only, but you can generalize)
    from forum.models import Message
    from forum.forms import MessageForm
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
        return redirect(request.path)

    context = {
        "post": post_obj,
        "messages": messages,
        "form": form,
        "parent_id": parent_id,
    }
    return render(request, template, context)
    