from django.urls import path
from django.conf.urls import url

from webapp.models import Post

from . import views

from django.contrib.auth import views as authViews

urlpatterns = [

    path('', views.index, name='index'),

    url(r'^webapp/(?P<pk>[0-9]+)/$', views.articles, name="articles"),

    path('exit/', authViews.LogoutView.as_view(template_name="webapp/exit.html"), name="exit"),

	path('authorization/', authViews.LoginView.as_view(template_name="webapp/authorization.html"), name="authorization"),
    path('registration/', views.registration, name="registration"),

    path('create/', views.create, name="create")
]