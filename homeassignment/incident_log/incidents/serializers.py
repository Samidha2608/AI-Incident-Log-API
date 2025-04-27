# Serializer to handle Incident model data for API communication


from rest_framework import serializers
from .models import Incident

# here i am creating a serializer called IncidentSerializer
# this will help in converting model data into json and vice versa

class IncidentSerializer(serializers.ModelSerializer):
    # here im defining severity choices manually
    # so user can only select from Low, Medium, High
    # cant send anything random in severity field

    SEVERITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    ]
    
    # here i am telling django that severity field should
    # be choice based not free text input

    severity = serializers.ChoiceField(choices=SEVERITY_CHOICES)
    
    # inside this Meta class we tell which model to use
    # and which fields to include in serializer

    class Meta:
        model = Incident
        fields = ['id', 'title', 'description', 'severity', 'reported_at']

        # here i made id and reported_at as read only
        # means user cannot edit these fields manually

        read_only_fields = ['id', 'reported_at']
