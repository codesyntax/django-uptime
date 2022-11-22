# django-uptime
Editable non-cached monitorization path for Django

Installation
------------

To install ``django_uptime`` simply run:

```bash

   pip install django-uptime
```

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

2. Include the desired url path into your projects main ``urls.py`` file:

```python

   from django.urls import include, path

   urlpatterns = [
      ...
      path('ok/', include('django_uptime.urls')),
      ...
   ]
```
