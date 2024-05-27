from rest_framework import serializers
from ..models import StudentList, Departments, Branches


class BranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branches
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Departments
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StudentList
        fields = '__all__'