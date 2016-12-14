from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.loginpage, name='loginpage'),
    url(r'^invalidlogin/$', views.invalidlogin, name='invalidlogin'),
    url(r'^loginauth/$', views.loginauth, name='loginauth'),
    url(r'^logoutpage/$', views.logoutpage, name='logoutpage'),
    url(r'^customer/(?P<cid>[0-9]+)/$', views.customerpage, name='customerpage'),
    url(r'^customer/(?P<cid>[0-9]+)/order/$', views.customerorder, name='customerorder'),
    url(r'^customer/(?P<cid>[0-9]+)/placeorder/$', views.placeorder, name="placeorder"),
    url(r'^customer/deleteorder/$', views.deleteorder, name="deleteorder"),
    url(r'^customer/changeorder/$', views.changeorder, name="changeorder"),
    url(r'^customer/fileupload/$', views.fileupload, name="fileupload"),
    url(r'^customer/fileupload/validate/$', views.fileuploadvalidate, name="fileuploadvalidate"),
    url(r'^customer/fileupload/process/$', views.fileuploadprocess, name="fileuploadprocess"),
    url(r'^vieworders/$', views.vieworders, name="vieworders"),
]
