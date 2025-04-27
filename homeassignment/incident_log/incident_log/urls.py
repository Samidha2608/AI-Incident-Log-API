"""
URL configuration for incident_log project.

# here im describing how url routing works in django for this project
# first the admin site route is set
# then i include the URLs for incidents app
# and finally root (/) redirects to incidents api

The `urlpatterns` list routes URLs to views. 
For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/

Examples:
Function views:
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')

Class-based views:
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

Including another URLconf:
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    # first path is admin panel for django
    path('admin/', admin.site.urls),
    
    # now we include our incidents app urls
    # this is where our api routes for incidents will live
    path('api/', include('incidents.urls')),
    
    # this path redirects the root of the site to incidents API
    # whenever someone goes to / it will send them straight to /api/incidents/
    path('', RedirectView.as_view(url='/api/incidents/')),
]
