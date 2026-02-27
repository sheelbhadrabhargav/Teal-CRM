from django.urls import path
from . import views

app_name = 'leads'
 
urlpatterns = [
    path('add-lead/', views.add_lead, name='add' ),
    path('<int:pk>/', views.lead_detail, name='detail'),
    path('<int:pk>/delete/', views.lead_delete, name="delete"),
    path('<int:pk>/edit/', views.lead_edit, name='edit'),
    path('<int:pk>/convert/', views.convert_to_client, name='convert'),
    path('lead-list/', views.lead_list, name='list'),
]
