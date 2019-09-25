from django.conf.urls import url
from . import views
from django.urls import path
from rest_framework.routers import DefaultRouter
from django.utils.translation import ugettext_lazy as _

app_name = 'accounts'
urlpatterns = [
    path(_(r'^login/$'),
        views.UserLoginView.as_view(),
        name='login'),
    url(r'add_book$', views.add_book, ),
    url(r'show_books$', views.show_books, ),

    # test ok
    url(r'test/', views.test, ),
    url(r'test-book/', views.test_book, ),
]

