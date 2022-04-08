from django.contrib import admin
from post.models import Topic, Comment

# Register your models here.
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    # 添加批量上线和批量下线的动作
    actions = ['topic_online', 'topic_offline']
    def topic_online(self, request, queryset):
        rows_updated = queryset.update(is_online=True)
        self.message_user(request, '{} topic is online'.format(rows_updated))
    topic_online.short_description = "上线所选的{}".format(Topic._meta.verbose_name)
    def topic_offline(self, request, queryset):
        row_updated = queryset.update(is_online=False)
        self.message_user(request, '{} topic is offline'.format(row_updated))
    topic_offline.short_description = "下线所选的{}".format(Topic._meta.verbose_name)

    # 设置显示属性内容
    list_display = ("topic_title", "topic_content", "topic_is_online", "topic_user", "topic_created_time")
    # 设置显示内容
    def topic_is_online(self, obj):
        return "是" if obj.is_online else "否"
    topic_is_online.short_description = "话题是否在线"
    def topic_content(self, obj):
        return obj.content[:30]
    topic_content.short_description = "话题内容"
    def topic_title(self, obj):
        return obj.title
    topic_title.short_description = "话题"
    def topic_user(self, obj):
        return obj.user
    topic_user.short_description = "用户"
    def topic_created_time(self, obj):
        return obj.created_time
    topic_created_time.short_description = "创建时间"

    # 添加搜索框
    search_fields = ['title', 'user__username']
    # 添加过滤器
    list_filter = ['title', 'user__username']
    # 添加排序
    ordering = ["id"]
    # 添加分页显示
    list_per_page = 1
    list_max_show_all = 2
    # 设置详情页显示内容, 如果元组组成的列，会显示在一行
    fields = [('user', 'title'), 'content', 'is_online']
    # 设置详情页过滤显示内容
    # exclude = ['content']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_up', 'comment_down', 'comment_content', 'comment_created_time')
    def comment_up(self, obj):
        return obj.up
    comment_up.short_description = '支持'
    def comment_down(sefl, obj):
        return obj.down
    comment_down.short_description = '反对'
    def comment_content(self, obj):
        return obj.content[:30]
    comment_content.short_description = "评论内容"
    def comment_created_time(self, obj):
        return obj.created_time
    comment_created_time.short_description = "创建时间"
    search_fields = ["content"]
    list_filter = ['content']