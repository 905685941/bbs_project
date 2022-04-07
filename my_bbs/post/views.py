from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from post.models import Topic, Comment
from post.post_service import build_topic_base_info, build_topic_detail_info, add_comment_to_topic

# Create your views here.
def topic_list_view(request):
    "话题列表"
    topic_qs = Topic.objects.all()
    result = {
        "count": topic_qs.count(),
        "info": [build_topic_base_info(topic) for topic in topic_qs]
    }
    return JsonResponse(result)


def topic_detail_view(request, topic_id):
    """话题详情"""
    result = []
    try:
        result = build_topic_detail_info(Topic.objects.get(pk=topic_id))
    except Topic.DoesNotExist:
        pass
    print(result)
    return JsonResponse(result)


@csrf_exempt
def add_comment_to_topic_view(request):
    """
    给话题添加评论
    """
    topic_id = int(request.POST.get("id",0))
    content = request.POST.get("content", "")
    topic = None
    try:
        topic = Topic.objects.get(pk=topic_id)
    except Topic.DoesNotExist:
        pass

    if topic and content:
        return JsonResponse({"id": add_comment_to_topic(topic, content).id})
    return JsonResponse({})
