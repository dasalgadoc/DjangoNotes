"""NotesProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

# Para Media
from django.conf import settings
from django.conf.urls.static import static

from post import views as posts_views
from users import views as users_views
from NotesProject import views as local_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^holaMundo/', local_views.holaMundo),
    url(r'^numeros/', local_views.numeros),
    url(r'^numerosJSON/', local_views.numerosJSON),
    url(r'^sorted/', local_views.sort_integers),
    url(r'^posts/', posts_views.list_post, name='feed'),
    url(r'^users/login/', users_views.login_view, name="login"),
    url(r'^users/logout/', users_views.logout_view, name="logout")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
