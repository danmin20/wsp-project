from django import forms
from django.db.models import fields
from .models import Post
from django.contrib.auth.models import User
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')