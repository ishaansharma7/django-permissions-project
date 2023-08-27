from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (LandingPageView, ResidentListView,
                    ResidentDetailView, ResidentDeleteView, ResidentCreateView,
                    ResidentUpdateView, CommListView, CommDetailView, CommCreateView,
                    CommDeleteView, CommUpdateView)
from django.views.generic import TemplateView


app_name = 'resident_app'

urlpatterns = [
    path('home/', LandingPageView.as_view(), name='home'),
    path('resident-list/', ResidentListView.as_view(), name='resident_list'),
    path('permission-denied/', TemplateView.as_view(template_name='resident_app/no_perm.html'), name='no_perm'),
    path('resident-detail/<int:pk>', ResidentDetailView.as_view(), name='resident_detail'),
    path('resident-delete/<int:pk>', ResidentDeleteView.as_view(), name='resident_del'),
    path('resident-create/', ResidentCreateView.as_view(), name='resident_create'),
    path('resident-update/<int:pk>', ResidentUpdateView.as_view(), name='resident_update'),

    #### community ####
    path('community-list/', CommListView.as_view(), name='comm_list'),
    path('community-detail/<int:pk>', CommDetailView.as_view(), name='comm_detail'),
    path('community-create/', CommCreateView.as_view(), name='comm_create'),
    path('community-delete/<int:pk>', CommDeleteView.as_view(), name='comm_del'),
    path('community-update/<int:pk>', CommUpdateView.as_view(), name='comm_update'),
]