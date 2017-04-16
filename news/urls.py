from django.conf.urls import url
from . import api

urlpatterns = [
    url(r'^whiteboard/grievance/$', api.GrievanceList.as_view()),
    url(r'^whiteboard/placement/$', api.PlacementList.as_view()),
    url(r'^whiteboard/newsfeed/$', api.NewsFeedList.as_view()),
    url(r'^whiteboard/notifications/$', api.GeneralNotificationList.as_view()),
    url(r'^whiteboard/login/$', api.receiveData),
    url(r'^whiteboard/assignments/$', api.student_assignments),
    url(r'^whiteboard/tests/$', api.student_tests),
    url(r'^whiteboard/private_grievances/$', api.private_grievance),
    url(r'^whiteboard/post_grievance/$', api.submit_grievance)
]
