from django.conf import settings
from django.contrib import admin
from django.urls import include, path
{%- if cookiecutter.use_rest_framework == 'y' %}
from rest_framework import routers
{%- endif %}

{%- if cookiecutter.use_rest_framework == 'y' %}

router = routers.DefaultRouter()
# router.register('',,base_ name='')
{%- endif %}

urlpatterns = [
    path(r'admin/doc/', include('django.contrib.admindocs.urls')),
    path(r'admin/', admin.site.urls),
    {%- if cookiecutter.use_rest_framework == 'y' %}
    path(r'api/', include(router.urls)),
    {%- endif %}
    path('', include('apps.{{ cookiecutter.repo_name }}.urls')),
]


if settings.DEBUG:
    import debug_toolbar  # noqa: Z435
    urlpatterns = [
        path(r'__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
