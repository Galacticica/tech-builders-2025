from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CommunityProjectForm

@login_required
def create_project(request):
    if request.method == "POST":
        form = CommunityProjectForm(request.POST, request.FILES)
        if form.is_valid():
            community_project = form.save(commit=False)
            community_project.author = request.user
            community_project.save()

            media_url = form.cleaned_data.get('media_url')
            media_type = form.cleaned_data.get('media_type')
            if media_url:
                from posts.models import Media
                title = f"{media_type.title()} for {community_project.title}" if media_type else None
                Media.objects.create(url=media_url, post=community_project, title=title)
            return redirect("my_profile")
    else:
        form = CommunityProjectForm()
    return render(request, "community_projects/create_project.html", {"form": form})

