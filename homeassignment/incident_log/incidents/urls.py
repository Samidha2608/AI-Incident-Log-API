from django.urls import path
from .views import IncidentList, IncidentDetail

# here i am creating a list called urlpatterns
# basically it will store all the url routes
# and tell django which view to call for which route

urlpatterns = [
    # in this path im defining 'incidents/' url
    # whenever user hits this url im calling IncidentList view
    # it will either show list of all incidents or let user create new one

    path('incidents/', IncidentList.as_view(), name='incident_list'),

    # here im defining another path with 'incidents/<int:pk>/'
    # <int:pk> means we expect an integer id in url
    # when user hits this url im calling IncidentDetail view
    # this view will either fetch that incident details
    # or delete that incident depending on method (get or delete)

    path('incidents/<int:pk>/', IncidentDetail.as_view(), name='incident_detail'),
]
