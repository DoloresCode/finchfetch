from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'), 
    path('about/', views.About.as_view(), name='about'), 
    path('microorganisms/', views.MicroorganismIndex.as_view(), name='microorganism_index'),
    path('microorganisms/new/', views.MicroorganismCreate.as_view(), name="microorganism_create"),
    path('microorganisms/<int:pk>/', views.MicroorganismDetail.as_view(), name="microorganism_detail"),
    path('microorganisms/<int:pk>/update',views.MicroorganismUpdate.as_view(), name="microorganism_update"),
    path('microorganisms/<int:pk>/delete', views.MicroorganismDelete.as_view(), name="microorganism_delete"),
    path('microorganisms/<int:pk>/culture_medias/new/', views.CultureMediaCreate.as_view(), name="culture_media_create"),
    path('collection/', views.Collection.as_view(), name='collection'),
    path('morphological_classifications/<int:pk>/culture_medias/<int:culture_media_pk>/', views.MorphologicalClassificationCultureMediaAssoc.as_view(), name="morphological_classification_culture_media_assoc"),
]
