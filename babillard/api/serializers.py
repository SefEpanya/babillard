from msilib.schema import Class
from pyexpat import model
from rest_framework import serializers
from .models import Client, Product


class ClientSerializer(serializers.ModelSerializer):
     class Meta:
        model= Client
        fields='__all__'

