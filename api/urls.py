from . import views
from django.urls import path
urlpatterns=[path('',views.submit_blog_post,name="blog_post")]