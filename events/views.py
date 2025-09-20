from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EventForm

@login_required
def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.save()

            media_url = form.cleaned_data.get('media_url')
            media_type = form.cleaned_data.get('media_type')
            if media_url:
                from posts.models import Media
                title = f"{media_type.title()} for {event.title}" if media_type else None
                Media.objects.create(url=media_url, post=event, title=title)
            return redirect("my_profile")
    else:
        form = EventForm()
    return render(request, "events/create_event.html", {"form": form})

