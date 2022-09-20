from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('errors/', views.errors_index, name='index'),
  path('errors/<int:error_id>/', views.errors_detail, name='error_detail'),
  path('errors/create/', views.ErrorCreate.as_view(), name='error_create'),
  path('errors/<int:pk>/update/', views.ErrorUpdate.as_view(), name='error_update'),
  path('errors/<int:pk>/delete/', views.ErrorDelete.as_view(), name='error_delete'),
  path('errors/<int:error_id>/add_comment/', views.add_comment, name='add_comment'),
]