from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

import ads.views.ad
from ads.views import cat, ad
from ads.views.ad import AdViewSet
from ads.views.cat import CatViewSet
from users.views import user, locations
from users.views.locations import LocViewSet

router = routers.SimpleRouter()
router.register('loc', LocViewSet)
router.register('cat', CatViewSet)
router.register('ad', AdViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', cat.index),
    path('ad_search/', ads.views.ad.AdListView.as_view()),
    path('user/', include('users.urls')),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)