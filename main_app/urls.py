from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'), 
    path('about/', views.About.as_view(), name='about'), 
    path('microorganisms/', views.MicroorganismIndex.as_view(), name='microorganism_index'),
    path('microorganisms/new/', views.MicroorganismCreate.as_view(), name="microorganism_create"),
    path('microorganisms/<int:pk>/', views.MicroorganismDetail.as_view(), name="microorganism_detail"),
    path('microorganisms/<int:pk>/update',views.MicroorganismUpdate.as_view(), name="microorganism_update"),
    path('microorganisms/<int:pk>/delete',views.MicroorganismDelete.as_view(), name="microorganism_delete"),
]