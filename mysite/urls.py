
from django.contrib import admin
from django.urls import path, include 

admin.site.site_header = "__ Admin"
admin.site.site_title = "__ Admin Portal"
admin.site.index_title = "Welcome to __ Portal"

admin.site.site_header = "Charu Trip Sheet Admin"
admin.site.site_title = "Charu Admin Portal"
admin.site.index_title = "Welcome to Trip Sheet Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authenticate.urls')),
]

