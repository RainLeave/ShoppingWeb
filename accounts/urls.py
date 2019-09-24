from django.conf.urls import url
from . import views

from rest_framework.routers import DefaultRouter
from django.utils.translation import ugettext_lazy as _

app_name = 'accounts'
urlpatterns = [
    url(_(r'^login/$'),
        views.UserLoginView.as_view(),
        name='login'),
    url(r'add_book$', views.add_book, ),
    url(r'show_books$', views.show_books, ),
]

