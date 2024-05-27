from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..models import StudentList, Departments, Branches
from .serializers import StudentSerializer, BranchSerializer, DepartmentSerializer

# Create your views here.

class BranchListView(APIView):
    # check the brach 'id' (pk) is exists or not
    def get(self, request, pk=None):
        if pk:
            branch_obj = get_object_or_404(Branches, pk=pk)
            serializer = BranchSerializer(branch_obj)
            return Response({'data': serializer.data, 'message': 'Branch data retrieved successfully'}, status=status.HTTP_200_OK)
        else:
            branch_obj = Branches.objects.all()
            serializer = BranchSerializer(branch_obj, many=True)
            return Response({'data': serializer.data, 'message': 'Branch data retrieved successfully'}, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = BranchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data, 'message': 'Branch data inserted successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def put(self, request, pk):
        branch_obj = get_object_or_404(Branches, pk=pk)
        serializer = BranchSerializer(branch_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data, 'message': 'Branch data updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    def delete(self, request, pk):
        branch_obj = get_object_or_404(Branches, pk=pk)
        branch_obj.delete()
        return Response({'message': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    


class DepartmentListView(APIView):
    def get(self, request, pk=None):
        if pk:
            depart_obj = get_object_or_404(Departments, pk=pk)
            serializer = DepartmentSerializer(depart_obj)
            return Response({'data': serializer.data, 'message': 'Department data retrieved successfully'}, status=status.HTTP_200_OK)
        else:
            depart_obj = Departments.objects.all()
            serializer = DepartmentSerializer(depart_obj, many=True)
            return Response({'data': serializer.data, 'message': 'Departments data retrieved successfully'}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data, 'message': 'Department data inserted successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        depart_obj = get_object_or_404(Departments, pk=pk)
        serializer = DepartmentSerializer(depart_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data, 'message': 'Department data updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        depart_obj = get_object_or_404(Departments, pk=pk)
        depart_obj.delete()
        return Response({'message': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    

class StudentListView(APIView):
    def get(self, request, pk=None):
        if pk:
            stud_obj = get_object_or_404(StudentList, pk=pk)
            serializer = StudentSerializer(stud_obj)
            return Response({'data': serializer.data, 'message': 'Student data retrieved successfully'}, status=status.HTTP_200_OK)
        else:
            stud_obj = StudentList.objects.all()
            serializer = StudentSerializer(stud_obj, many=True)
            return Response({'data': serializer.data, 'message': 'Students data retrieved successfully'}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data, 'message': 'Student data inserted successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        stud_obj = get_object_or_404(StudentList, pk=pk)
        serializer = StudentSerializer(stud_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data, 'message': 'Student data updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        stud_obj = get_object_or_404(StudentList, pk=pk)
        stud_obj.delete()
        return Response({'message': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)




































































# class DepartmentListView(APIView):
#     # To check the student department 'id' is exists or not
#     def get_object(self, pk):
#         try:
#             return Departments.objects.get(pk=pk)
#         except:
#             return Response({'message':"no department exists"}, status=status.HTTP_400_BAD_REQUEST)
        
#     def get(self, request, pk):
#         depart_obj = self.get_object(pk)
#         serializer = DepartmentSerializer(depart_obj)
#         return Response({'data': serializer.data, 'message': 'Department data retrieved successfully'}, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         serializer = DepartmentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'data': serializer.data, 'message': 'Department data Inserted successfully'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk):
#         depart_obj = self.get_object(pk)
#         serializer = DepartmentSerializer(depart_obj, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'data': serializer.data, 'message': 'Department data updated successfully'}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         depart_obj = self.get_object(pk)
#         depart_obj.delete()
#         return Response({'message': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    


# class StudentListView(APIView):
#     # To check the student 'id' is exists or not
#     def get_object(self, pk):
#         try:
#             return StudentList.objects.get(pk=pk)
#         except:
#             return Response({'message':"no student exists"}, status=status.HTTP_400_BAD_REQUEST)

#     def get(self, request, pk):
#         stud_obj = self.get_object(pk)
#         serializer = StudentSerializer(stud_obj)  
#         return Response({'data': serializer.data, 'message': 'Student data retrieved successfully'}, status=status.HTTP_200_OK)  
    
#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'data': serializer.data, 'message': 'Department data Inserted successfully'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def put(self, request, pk):
#         stud_obj = self.get_object(pk)
#         serializer = StudentSerializer(stud_obj, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'data': serializer.data, 'mesaage': 'Student data Updated succcessfully'}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         stud_obj = self.get_object(pk)
#         stud_obj.delete()
#         return Response({'message': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)





