from django.contrib import admin
from django.urls import path, include # neeed to import inclde
from django.conf import settings
from django.conf.urls.static import static #imports static 
import jobs.views #imports views.py fom jobs

urlpatterns = [
    path('admin/', admin.site.urls), #access to admin
    path('', jobs.views.home, name='home'), #go to jobs.views home function
    path('blog/', include('blog.urls')) #forwards request to blog urls.py
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #image views