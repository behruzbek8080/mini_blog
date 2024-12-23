from django.urls import path
from .views import home_view, register_view, login_view, profile_view, logout_view, edit_profile_view, blog_view, blog_detail_view, create_blog_view 
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', blog_view, name='home'),
    path('blog/<int:pk>/', blog_detail_view, name='blog_detail'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),
    path('profile/edit/', edit_profile_view, name='edit-profile'),
    path('blog/<int:pk>/', blog_detail_view, name='blog_detail'),
    path('create_blog/', create_blog_view, name='create_blog'),# type: ignore
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)