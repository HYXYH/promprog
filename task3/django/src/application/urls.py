"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from todolist.api.viewsets import TaskViewSet
from django.views.generic import TemplateView
from rest_framework import routers
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    url(r'^api/',  include((router.urls, 'api'), namespace='api')),
    url('admin/', admin.site.urls),
    url(r'old/', TemplateView.as_view(template_name='todolist/todolist.html')),
    url(r'', TemplateView.as_view(template_name='todolist/core.html')),
]

#
# if settings.DEBUG is True:
#     from django.conf.urls.static import static
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#
