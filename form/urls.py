from django.urls import path
from django.urls.resolvers import URLPattern
from .import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns =[
    path('',views.index,name='index'),
    path('contactus',views.contact,name='contactus'),
    path('register',views.register,name='register'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('user_login',views.user_login,name='user_login'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('password',views.change_password,name="password"),
    path('myblog',views.myblog,name='myblog'),
    path('image_upload',views.image_upload,name="image_upload"),
    path('myblogupdate/<int:todo_id>',views.myblogupdate,name='myblogupdate'),
    path('myblogdelete/<int:todo_id>',views.myblogdelete,name='myblogdelete'),
    path('image_download',views.image_download,name='image_download'),
    path('profile',views.profile,name="profile"),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)