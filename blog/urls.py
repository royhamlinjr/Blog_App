from django.urls import path
from . import views

app_name='blog'

urlpatterns=[
    path("",views.index),
    path('post/<slug:slug>',views.detail,name='detail'),

    # Redirection Pages 
    # path('new_url',views.new_url,name="newpage"),
    # path('old_url',views.old_url,name="oldpage"),

    path('contact',views.contact_view,name='contact'),
    path('about',views.about_page,name='about'),
]