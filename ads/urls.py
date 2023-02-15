from django.urls import path

from ads.views import cat, ad

urlpatterns = [
    path('', ad.AdListView.as_view()),
    path('<int:pk>/', ad.AdDetailView.as_view()),
    path('create/', ad.AdCreateView.as_view()),
    path('<int:pk>/update/', ad.AdUpdateView.as_view()),
    path('<int:pk>/delete/', ad.AdDeleteView.as_view()),
    path('<int:pk>/image/', ad.AdImageView.as_view()),
    path('cat/', cat.CategoriesListView.as_view()),
    path('cat/<int:pk>/', cat.CategoryDetailView.as_view()),
    path('cat/create/', cat.CategoriesCreateView.as_view()),
    path('cat/<int:pk>/delete/', cat.CategoriesDeleteView.as_view()),
    path('by_user/', ad.AuthorAdDetailView.as_view())
]