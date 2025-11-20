
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin-web/', admin.site.urls),
    path('', include ('home.urls')),
    path('login/', include ('contas.urls'))
]
