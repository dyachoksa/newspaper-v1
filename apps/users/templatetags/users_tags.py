from django import template
from django.urls import reverse

register = template.Library()


@register.filter
def user_detail_url(user):
    return reverse("users:detail", args=(user.pk,))


@register.filter
def author_detail_url(user):
    return reverse("author", args=(user.pk,))
