from rest_framework import serializers
from ..models import Books


# Create your serializers here.

class BooksSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Books
        fields = '__all__'


