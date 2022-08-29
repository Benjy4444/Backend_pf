"""Posts URLs."""

# Django
from django.urls import path


# Views
from posts import views

urlpatterns = [
    path(
        route='noticias',
        view=views.PostsFeedView.as_view(template_name='noticias.html'),
        name='noticias'
    ),

    path(
        route='',
        view=views.PostsFeedView.as_view(template_name='index.html'),
        name='index'
    ),
    path(
        route='posts/<slug:url>/',
        view=views.PostDetailView.as_view(),
        name='detail'
    ),
    path(
        route='posts/save_comment',
        view=views.save_comment,
        name='save_comment'
    ),

]