from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

from account import views as A
from post import views as P

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', P.main, name="home"),
    # path('account/', include('account.urls')),
    path('post/', include('post.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
