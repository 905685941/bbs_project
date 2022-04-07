from post.models import Comment

def add_comment_to_topic(topic, content):
    """
    给topic添加评论
    """
    return Comment.objects.create(topic=topic, content=content)


def build_topic_base_info(topic):
    """
    构造Topic基本信息
    """
    return {
        "id": topic.id,
        "title": topic.title,
        "user": topic.user.username,
        "created_time": topic.created_time
    }


def build_comment_info(comment):
    """
    构造Comment信息
    """
    return {
        "id": comment.id,
        "content": comment.content,
        "up": comment.up,
        "down": comment.down,
        "created_time": comment.created_time,
        "last_modified": comment.last_modified
    }


def build_topic_detail_info(topic):
    """
    构造topic详情信息
    """
    print(topic.title)
    comment_qs = Comment.objects.filter(topic=topic)
    return {
        "id": topic.id,
        "title": topic.title,
        "content": topic.content,
        "user": topic.user.username,
        "created_time": topic.created_time,
        "last_modified": topic.last_modified,
        "comments": [build_comment_info(comment) for comment in comment_qs]
    }