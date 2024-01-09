from rest_framework import serializers
from Api.models import CollegeModel,StudentModel

class CollegeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CollegeModel
        fields = "__all__"
class StudentSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model=StudentModel
        fields="__all__"