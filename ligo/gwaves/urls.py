from django.urls import path
from . import views

urlpatterns = [
    path('', views.gwave_index, name='gwave_index'),
    path('view/<int:gwave_id>/', views.gwave_view, name='gwave_view'),
    path('new', views.gwave_new, name='gwave_new'),
    path('edit/<int:gwave_id>/', views.gwave_edit, name='gwave_edit'),
    path('delete/<int:gwave_id>/', views.gwave_delete, name='gwave_delete'),
]
