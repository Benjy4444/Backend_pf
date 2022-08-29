from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from posts.views import searchBlog


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('posts.urls', 'posts'), namespace='posts')),
    path(
        route='noticias',
        view=TemplateView.as_view(template_name='noticias.html'),
        name='noticias'
    ),
    path(
        route='',
        view=TemplateView.as_view(template_name='index.html'),
        name='index'
    ),
    path(
        route='institucional',
        view=TemplateView.as_view(template_name='about.html'),
        name='about'
    ),
    path(
        route='categorias',
        view=TemplateView.as_view(template_name='categorias.html'),
        name='categorias'
    ),
    path(
        route='contacto',
        view=TemplateView.as_view(template_name='contacto.html'),
        name='contacto'
    ),
    path('', include(('users.urls', 'users'), namespace='users')),

    path("q/", searchBlog, name='search'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

