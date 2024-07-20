
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from main.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('add',add),
    path('edit/<int:post_id>',edit_post),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)