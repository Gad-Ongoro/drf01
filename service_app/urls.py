from django.urls import path, include
from . import views

urlpatterns = [
    # user routes
    path('users/', views.UserListCreate.as_view()),
    path('users/<int:pk>/', views.UserDetailView.as_view()),
    
    # service routes
    path('services/', views.ProductListCreate.as_view()),
    path('services/<int:pk>/', views.ProductDetailView.as_view()),
    
    # booking routes
    path('bookings/', views.OrderListCreate.as_view()),
    path('bookings/<int:pk>/', views.OrderDetailView.as_view()),
    
    # review routes
    path('reviews/', views.ReviewListCreate.as_view()),
    path('reviews/<int:pk>/', views.ReviewDetailView.as_view()),

]
