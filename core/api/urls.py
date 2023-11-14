from django.urls import path, include
from .views import MusicView

urlpatterns = [
    path('music', MusicView.as_view({
        'get': 'list',
    })),
    path('api-auth/', include('rest_framework.urls'))
]
