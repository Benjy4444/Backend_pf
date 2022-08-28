from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('posts.urls', 'posts'), namespace='posts')),
    path(
        route='noticias',
        view=TemplateView.as_view(template_name='posts/index.html'),
        name='noticias'
    ),
    path(
        route='home',
        view=TemplateView.as_view(template_name='index.html'),
        name='index'
    ),
    path(
        route='institucional',
        view=TemplateView.as_view(template_name='about.html'),
        name='about'
    ),
    path('', include(('users.urls', 'users'), namespace='users')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

