from rest_framework import serializers
from .models import Email

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Email 
        fields=('Subject','From','To','Cc','Bcc','Content')