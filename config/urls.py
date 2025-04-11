from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', include('src.accounts.urls')),
    path('api/profile/', include('src.users.urls')),
    path('api/reward/', include('src.rewards.urls'))
]