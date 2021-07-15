from django.urls import path, include
from leads.views import lead_list, lead_detail, lead_create, lead_update, lead_delete
from leads.views import LeadListView, LeadDetailView, LeadCreateView, LeadDeleteView

app_name = 'leads'

urlpatterns = [
    # Class based url-view

    path('list/', LeadListView.as_view(), name='lead-list'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('create/', LeadCreateView.as_view(), name='lead-create'),
    path('<int:pk>/update/', lead_update, name='lead-update'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'),



    # Function based url-view
    
    # path('list/', lead_list, name='lead-list'),
    # path('<int:pk>/', lead_detail, name='lead-detail'),
    # path('create/', lead_create, name='lead-create'),
    # path('<int:pk>/update/', lead_update, name='lead-update'),
    # path('<int:pk>/delete/', lead_delete, name='lead-delete'),
]