"""surfhouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import main_app.views as main_app

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main_app.main),
    url(r'^catalog/', main_app.catalog),
    url(r'^contacts/', main_app.contacts),
    url(r'^long1', main_app.long1),
    url(r'^long2', main_app.long2),
    url(r'^long3', main_app.long3),
    url(r'^long4', main_app.long4),
]
