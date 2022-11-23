from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.views.generic import ListView
from django.conf import settings


class IndexView(ListView):
    model = ContentType
    template_name = "django_uptime/index.html"

    def get_queryset(self):
        ct_count = ContentType.objects.all().count()
        return ct_count

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context
