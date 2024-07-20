from django.urls import path, include
from . import views

urlpatterns = [
    # user routes
    path('users/', views.UserListCreate.as_view()),
    path('users/<int:pk>/', views.UserDetailView.as_view()),
    
    # service routes
    path('services/', views.ServiceListCreate.as_view()),
    path('services/<int:pk>/', views.ServiceDetailView.as_view()),
    
    # booking routes
    path('bookings/', views.BookingListCreate.as_view()),
    path('bookings/<int:pk>/', views.BookingDetailView.as_view()),
    
    # review routes
    path('reviews/', views.ReviewListCreate.as_view()),
    path('reviews/<int:pk>/', views.ReviewDetailView.as_view()),

]
