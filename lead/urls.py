from django.urls import path
from . import views
urlpatterns = [
    path('add-lead/', views.add_lead, name='add_lead' ),
    path('<int:pk>/', views.lead_detail, name='lead_detail'),
    path('<int:pk>/delete/', views.lead_delete, name="lead_delete"),
    path('<int:pk>/edit/', views.lead_edit, name='lead_edit'),
    path('<int:pk>/convert/', views.convert_to_client, name='lead_convert'),
    path('lead-list/', views.lead_list, name='lead_list'),
]
