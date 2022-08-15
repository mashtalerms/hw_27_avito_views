from django.contrib import admin
from django.urls import path
from ads.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('ad/', AdView.as_view(), name="ads_view"),
    path('ad/<int:pk>/', AdDetailView.as_view(), name="ad_view"),
    path('cat/', CategoryView.as_view(), name="cats_view"),
    path('cat/<int:pk>/', CategoryDetailView.as_view(), name="cat_view"),
]
