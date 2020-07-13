from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        min_length=10,
        max_length=600,
        label="",
        widget=forms.Textarea(attrs={"rows": 3}),
    )

    class Meta:
        model = Comment
        fields = ("content",)
