from django.contrib import admin
from django.urls import path

from index.views import index_views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', index_views),
]
