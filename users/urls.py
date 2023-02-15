from django.urls import path

from users.views import user, locations

urlpatterns = [
    path('', user.UserListView.as_view()),
    path('<int:pk>/', user.UserDetailView.as_view()),
    path('create/', user.UserCreateView.as_view()),
    path('<int:pk>/update/', user.UserUpdateView.as_view()),
    path('<int:pk>/delete/', user.UserDeleteView.as_view()),
    path('loc/', locations.LocListView.as_view()),
    path('loc/create/', locations.LocCreateView.as_view()),
    path('loc/<int:pk>/', locations.LocDetailView.as_view()),
    path('loc/<int:pk>/delete/', locations.LocDeleteView.as_view()),
]