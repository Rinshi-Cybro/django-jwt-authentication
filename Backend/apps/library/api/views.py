from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import BooksSerializer
from ..models import Books


# Create your views here.

class BooksListView(APIView):
    def get(self, request, pk=None):
        if pk:
            book_obj = get_object_or_404(Books, pk=pk)
            serializer = BooksSerializer(book_obj)
            return Response({'data': serializer.data, 'message': 'Retrieved successfully'}, status=status.HTTP_200_OK)
        else:
            book_obj = Books.objects.all()
            serializer = BooksSerializer(book_obj, many=True)
            return Response({'data': serializer.data, 'message': 'Retrieved successfully'}, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data, 'message': 'Data inserted successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        book_obj = get_object_or_404(Books, pk=pk)
        serializer = BooksSerializer(book_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data, 'message': 'Data Updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        book_obj = get_object_or_404(Books, pk=pk)
        book_obj.delete()
        return Response({'message': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)







