from django.urls import path

from ads.views import ad

urlpatterns = [
    path('', ad.AdListView.as_view()),
    path('<int:pk>/', ad.AdDetailView.as_view()),
    path('create/', ad.AdCreateView.as_view()),
    path('<int:pk>/update/', ad.AdUpdateView.as_view()),
    path('<int:pk>/delete/', ad.AdDeleteView.as_view()),

]