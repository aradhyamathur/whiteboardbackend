from rest_framework import serializers
from .models import Grievance, Placement, NewsFeed, Assignments, StudentTest


class GrievanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grievance
        fields = '__all__'


class PlacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placement
        fields = '__all__'


class NewsFeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsFeed
        fields = '__all__'


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignments
        fields = '__all__'


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTest
        fields = '__all__'