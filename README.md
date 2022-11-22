# django-uptime
Editable non-cached monitorization path for Django

Configuration
-------------

We need to hook ``django-uptime`` into our project.

1. Put ``django_uptime`` into your ``INSTALLED_APPS`` at settings module:

```python

   INSTALLED_APPS = (
       # other apps
       "django_uptime",
   )
```
