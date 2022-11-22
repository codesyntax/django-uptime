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

Put ``django_uptime`` into your ``INSTALLED_APPS`` at settings module:

```python

   INSTALLED_APPS = (
       # other apps
       "django_uptime",
   )
```
