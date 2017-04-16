from rest_framework.generics import ListCreateAPIView
from .models import Grievance, Placement, NewsFeed, WhiteBoardUser, StudentTest
from .serialysers import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import ast
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pprint


class GrievanceList(ListCreateAPIView):
    queryset = Grievance.objects.filter(grievance_permission='approved', grievance_type='public')
    serializer_class = GrievanceSerializer

    def perform_create(self, serializer):
        data = self.request.data
        print data
        ser = GrievanceSerializer(data={'subject': self.request.data['subject'],
                                        'info': self.request.data['info']})
        if ser.is_valid():
                ser.save()


class PlacementList(ListCreateAPIView):
    queryset = Placement.objects.all()
    serializer_class = PlacementSerializer


class NewsFeedList(ListCreateAPIView):
    queryset = NewsFeed.objects.filter(news_type='event')
    serializer_class = NewsFeedSerializer


class GeneralNotificationList(ListCreateAPIView):
    queryset = NewsFeed.objects.filter(news_type='notice')
    serializer_class = NewsFeedSerializer




@csrf_exempt
def receiveData(request):
    data = request.POST.get('data', None)
    if data is not None:
        info_list = ast.literal_eval(str(data))
        info_dict = dict(info_list[0])
        print info_dict['Name']
        print info_dict['Email']
        try:
            user = WhiteBoardUser.objects.get(email=info_dict['Email'])
            if user:
                return HttpResponse('Valid')
        except Exception as e:
            print e
            return HttpResponse('Invalid')

    else:
        return HttpResponse('no data received')


@api_view(['POST', 'GET'])
def student_assignments(request):
    if request.method == 'POST':
        data = request.data
        print data
        user = WhiteBoardUser.objects.get(email=data[0]['email'])
        assignments = Assignments.objects.filter(stream=user.stream)
        serializer = AssignmentSerializer(assignments, many=True)
        return Response(serializer.data)
    if request.method == 'GET':
        pprint.pprint(repr(request.__dict__))
        pprint.pprint(request.META)

        print request.data
        data = request.GET
        print data
        user = WhiteBoardUser.objects.get(email=data['email'])
        assignments = Assignments.objects.filter(stream=user.stream)
        # assignments = Assignments.objects.all()
        serializer = AssignmentSerializer(assignments, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def submit_grievance(request):
    data = request.data
    print data
    print data['email']
    complainer = WhiteBoardUser.objects.get(email=data['email'])
    gsubject = data['title']
    print complainer
    info = data['info']
    print gsubject, info
    grievance = GrievanceSerializer(data={'user': complainer.id,
                                    'subject': gsubject, 'info': info})
    print grievance
    if grievance.is_valid(raise_exception=True):
        grievance.save()
        return Response(grievance.data, status=201)
    return Response("Error", status=400)


@api_view(['POST', 'GET'])
def student_tests(request):
    if request.method == 'POST':
        data = request.data
        print data
        user = WhiteBoardUser.objects.get(email=data[0]['email'])
        tests = StudentTest.objects.filter(stream=user.stream)
        serializer = TestSerializer(tests, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def private_grievance(request):
    if request.method == 'POST':
        data = request.data
        print data
        user = WhiteBoardUser.objects.get(email=data[0]['email'])
        private_gre = Grievance.objects.filter(user=user)
        serializer = GrievanceSerializer(private_gre, many=True)
        return Response(serializer.data)
