from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^english/$', views.english, name='ura'),
    url(r'^test$', views.test, name='test'),
    url(r'^register/$', views.RegisterFormView.as_view(), name='reg'),
    url(r'^add/$', views.add, name='add'),
    url(r'^login/$', views.LoginFormView.as_view(), name='log'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
]