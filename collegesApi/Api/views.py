from django.shortcuts import render

from rest_framework import viewsets
from Api.models import CollegeModel,StudentModel
from Api.serializers import CollegeSerializer,StudentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class CollegeViewSet(viewsets.ModelViewSet):
    queryset = CollegeModel.objects.all()
    serializer_class = CollegeSerializer

    @action(detail=True,methods=['get'])
    def students(self,request,pk=None):
        try:
            college=CollegeModel.objects.get(pk=pk)
            students = StudentModel.objects.filter(college = college)
            stud_serializer = StudentSerializer(students,many = True,context = {'request':request})
            return Response(stud_serializer.data)
        except Exception as e:
            return Response({"error":"This College Id is not in Database !!!"},status=404)
        
class StudentViwSet(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer