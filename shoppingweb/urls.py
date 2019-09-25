"""shoppingweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
# from django.views.generic import templateview
from orders import views
# import goods.urls

# media file's url
from django.conf import settings
from django.conf.urls.static import static
from lufei import views
from accounts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    # Add for rest framework
    path(r'^api-auth/', include('rest_framework.urls')),
    # Add for vue
    # url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^api/v1/accounts/', include('accounts.urls')),  # include 路由转发
    # order
    # path(r'^dog/', views.DogView.as_view()),
    # 用户认证 基于token 如果登录成功则url可以访问，返回元组，否则报错
    # path(r'^login', views.MyAuthentication),

    # test
    # path(r'^api/v1/accounts/', include('accounts.urls', namespace='shop-acccounts')),

]


# set the path for media
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)