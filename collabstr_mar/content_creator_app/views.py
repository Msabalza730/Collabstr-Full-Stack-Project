from django.shortcuts import render
from django.http import JsonResponse
from .models import *


def content_list(request):
    """View to show the info about content creators"""
    content_objects = Content.objects.select_related('creator').all()[:30]
    creators = Creator.objects.all()

    context = {
        'content_objects': content_objects,
        'creators': creators,
    }
    return render(request, 'home.html', context)


def filter_by_platform(request):
    """View to show the filter"""
    platform = request.GET.get('platform')
    content_objects = Content.objects.select_related('creator').filter(creator__platform=platform)[:30]

    data = []
    for content in content_objects:
        data.append({
            'url': content.url,
            'creator_name': content.creator.name,
            'creator_rating': content.creator.rating,
        })

    return JsonResponse(data, safe=False)

