from django.urls import path
from .views import AdminSignupView, AdminLoginView, BookCreateView, BookListView, BookUpdateView, BookDeleteView, HomeView
urlpatterns = [
    path('api/admin/signup/', AdminSignupView.as_view(), name='admin-signup'),
    path('api/admin/login/', AdminLoginView.as_view(), name='admin-login'),
    path('api/admin/book/create/', BookCreateView.as_view(), name='book-create'),
    path('api/admin/book/list/', BookListView.as_view(), name='book-list'),
    path('api/admin/book/update/<int:id>/', BookUpdateView.as_view(), name='book-update'),
    path('api/admin/book/delete/<int:id>/', BookDeleteView.as_view(), name='book-delete'),
    path('',HomeView, name='home'),
    
]
