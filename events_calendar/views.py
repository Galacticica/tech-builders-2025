from django.http import JsonResponse
from django.shortcuts import render
from events.models import Event
from community_projects.models import CommunityProject


def calendar_view(request):
    return render(request, "events_calendar/calendar.html")

def event_json(request):
    events = Event.objects.all()
    community_projects = CommunityProject.objects.all()
    all_items = sorted(
        list(events) + list(community_projects),
        key=lambda item: item.created_at,
        reverse=True
    )
    data = []
    for post in all_items:
        url = f"/{post.slug}/"
        data.append({
            "title": post.title or "Event",
            "start": post.date_of_event.isoformat() if hasattr(post, 'date_of_event') and post.date_of_event else None,
            "url": url,
        })
    return JsonResponse(data, safe=False)
