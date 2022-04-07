from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BaseModel(models.Model):
    """
    post 应用中的基类
    """
    class Meta:
        abstract = True
        ordering = ["-created_time"]
    created_time = models.DateTimeField(auto_now_add=True, help_text="创建时间")
    last_modified = models.DateTimeField(auto_now=True, help_text="修改时间")
    def __str__(self):
        raise NotImplementedError

class Topic(BaseModel):
    """
        BBS论坛发布的话题
    """
    title = models.CharField(max_length=255, unique=True, help_text="话题标题")
    content = models.TextField(help_text="话题内容")
    is_online = models.BooleanField(default=True, help_text="话题是否在线")
    user = models.ForeignKey(to=User, to_field="id", on_delete=models.CASCADE, help_text="关联用户表")
    def __str__(self):
        return "{}: {}".format(self.id, self.title[0:20])
    
    class Meta:
        verbose_name = '话题'
        verbose_name_plural = "话题"

class Comment(BaseModel):
    """
    BBS 话题评论
    """
    content = models.CharField(max_length=255, help_text="话题评论")
    topic = models.ForeignKey(to=Topic, to_field="id", on_delete=models.CASCADE, help_text="关联话题表")
    up = models.IntegerField(default=0, help_text="支持")
    down = models.IntegerField(default=0, help_text="反对")
    def __str__(self):
        return "{}: {}".format(self.id, self.content[0:20])

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = "评论"
