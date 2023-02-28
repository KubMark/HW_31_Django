from django.urls import path

from users import views

urlpatterns = [
    path('', views.UserListView.as_view(), name='user_list'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('create/', views.UserCreateView.as_view(), name='user_detail'),
    path('<int:pk>/update/', views.UserUpdateView.as_view(), name='user_update'),
    path('<int:pk>/delete/', views.UserDeleteView.as_view(), name='user_delete'),
    # path('loc/', views.LocationListView.as_view()),
    # path('create/', views.LocationCreateView.as_view(), name='loc_create'),
    # path('loc/<int:pk>/', views.LocationDetailView.as_view(), name='loc_detail'),
    # path('loc/<int:pk>/delete/', views.LocationDeleteView.as_view(), name='user_delete'),

]