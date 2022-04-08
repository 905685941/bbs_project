from xml.etree.ElementTree import Comment
from django import forms

from post.models import Topic

class TopicSearchForm(forms.Form):
    title = forms.CharField(label="Topic title")
    # 自定义校验规则
    def clean_title(self):
        title = self.clean_data.get("title")
        if len(title) < 5:
            raise forms.ValidationError("话题长度太短")
        return title

# 基于model的表单
class TopicModelForm(forms.ModelForm):
    class Meta:
        model = Topic
        exclude = ("is_online", "user")

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment