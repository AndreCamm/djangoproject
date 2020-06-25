from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cage/', include('cage.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#added these lines to redirect for images
#from django.conf import settings
#from django.conf.urls.static import static
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)