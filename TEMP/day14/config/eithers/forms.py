from django.forms import ModelForm
from .models import *
class CreateModelForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'