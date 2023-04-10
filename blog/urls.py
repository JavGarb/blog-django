from django.urls import path
from .views import blogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name="blog"

urlpatterns = [
    path('', blogListView.as_view(), name='home'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', BlogUpdateView.as_view(), name='update'), 
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name='delete'),   
]