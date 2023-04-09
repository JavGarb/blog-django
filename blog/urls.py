from django.urls import path
from .views import blogListView, BlogCreateView

app_name="blog"

urlpatterns = [
    path('', blogListView.as_view(), name='home'),
    path('create/', BlogCreateView.as_view(), name='create'),    
]