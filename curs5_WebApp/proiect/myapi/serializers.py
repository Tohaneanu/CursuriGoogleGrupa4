from rest_framework import serializers
from myapi.models import Employee


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('name', 'alias')
