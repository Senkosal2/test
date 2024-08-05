from rest_framework.response import Response
from rest_framework import viewsets,status
from rest_framework.decorators import action
from student.models import Student
from student.serializers import StudentSerializer

# Create your views here.
class StudentView(viewsets.ViewSet):
    
    @action(detail=False, methods=['get'])
    def get_students(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['get'])
    def get_student(self, request, pk):
        try:
            queryset = Student.objects.get(pk = pk)
            serializer = StudentSerializer(queryset, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=False, methods=['post'])
    def create_student(self, request):
        Student(
            name = request.data['name'],
            gender = request.data['gender'],
            dob = request.data['dob']
        ).save()
        return Response(status=status.HTTP_201_CREATED)
        
    @action(detail=True, methods=['put'])
    def update_student(self, request):
        try:
            student = Student.objects.get(pk = request.data['id'])
            student.name = request.data['name']
            student.gender = request.data['gender']
            student.dob = request.data['dob']
            student.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 
        
    @action(detail=True, methods=['delete'])
    def delete_student(self, request, pk):
        try:
            Student.objects.get(pk=pk).delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
            