
from django.shortcuts import get_object_or_404, render
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
    if post.post_type == 'event':
        template = "events/view_event.html"
    elif post.post_type == 'community_project':
        template = "community_projects/view_project.html"
    elif post.post_type == 'creation':
        template = "creations/view_creation.html"
    else:
        template = "feed/post_detail.html"
    return render(request, template, {
        "post": post
    })
    