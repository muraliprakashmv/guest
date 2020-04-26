from django.conf.urls import url

from webapp import views

urlpatterns=[

    url(r'^signup$',views.Signup,name="Signup"),
    url(r'^signin$',views.Signin,name="Signin"),
    url(r'^dashBoard$',views.dashBoard,name="dashBoard"),
    url(r'^$',views.dashBoard,name="dashBoard"),

    url(r'^signout$',views.Signout,name="Signout"),

    url(r'^create$',views.create,name='create'),
    url(r'^index$',views.index,name='index'),
    url(r'^update/(?P<pk>[0-9]+)$',views.update,name='update'),  #()-block (a+b)+(c) <pk> primarykey p is mandidatory
    url(r'^delete/(?P<pk>[0-9]+)$',views.delete,name='delete'),
    url(r'^view/(?P<pk>[0-9]+)$',views.view,name='view'),

]