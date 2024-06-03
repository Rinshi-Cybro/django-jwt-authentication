from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import BookSerializer
from ..models import Books


# Create your views here.

class BookListView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            book = Books.objects.all()
            serializer = BookSerializer(book, many=True)
            return Response(serializer.data)
        except:
            return Response({'msg':'Book list not found'})


class BooksView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, pk):
        try:
            book = Books.objects.get(id=pk)
            serializer = BookSerializer(book, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'msg': 'Book details not found'})


    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def put(self, request, pk):
        book = Books.objects.get(id=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid(raise_exception= True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk):
        try:
            book = Books.objects.get(id=pk)
            book.delete()
            return Response({'msg': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({'msg': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)







