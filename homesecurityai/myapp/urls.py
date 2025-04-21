from django.contrib import admin
from django.urls import path,include

from myapp import views

urlpatterns = [
    path('', views.login),
    path('admin_home', views.admin_home),
    path('manage_police_station', views.manage_police_station),
    path('add_new', views.add_new),
    path('send_reply', views.send_reply),
    path('view_complaint', views.view_complaint),
    path('view_police_station', views.view_police_station),
    path('reply_send', views.reply_send),

    path('view_user', views.view_user),



    path('police_home',views.police_home),
    path('police_view_report', views.police_view_report),
    path('reply_police', views.reply_police),
    path('send_reply', views.send_reply),
    path('complaint_police', views.complaint_police),
    path('login_post', views.login_post),
    path('add_new_post',views.add_new_post),

]
