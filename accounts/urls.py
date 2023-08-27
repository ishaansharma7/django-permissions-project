from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import index, RegisterView, test_restricted_view, CustomLoginView


app_name = 'accounts_app'

urlpatterns = [
    path('index/', index, name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='accounts_app:login'), name='logout'),
    path('test/restricted-view/', test_restricted_view, name='test_restricted_view')
]