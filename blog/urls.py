from django.urls import path, include
from django.contrib import admin
from .views import signup_view
from . import views

urlpatterns = [
    path('', views.post_list, name='postlist'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', signup_view, name='signup'),

]

