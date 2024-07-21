from django.shortcuts import render
from rest_framework import generics
from . import models
from . import serializers

# Create your views here.
# user views
class UserListCreate(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    
# profile views
class ProfileList(generics.ListAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

# service views
class ServiceListCreate(generics.ListCreateAPIView):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer
    
class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer

# booking views
class BookingListCreate(generics.ListCreateAPIView):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer
    
class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer
    
# review views
class ReviewListCreate(generics.ListCreateAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    
class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer