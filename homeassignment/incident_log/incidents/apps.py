from django.apps import AppConfig

# this file basically tells django that we have an app called incidents
# and here we configure basic settings for it

class IncidentsConfig(AppConfig):
    # setting default primary key type for models inside this app
    default_auto_field = 'django.db.models.BigAutoField'

    # setting name of the app so django knows about it
    name = 'incidents'
