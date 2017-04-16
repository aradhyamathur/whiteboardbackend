from __future__ import unicode_literals

from django.db import models


class WhiteBoardUser(models.Model):
    name = models.CharField(max_length=255)
    token = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    type = models.CharField(max_length=50, default="Student")
    uid = models.TextField(blank=True)
    stream = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.email


class Grievance(models.Model):

    subject = models.CharField(max_length=255, default='Grievance')
    info = models.TextField(null=True, blank=True)
    date_info = models.DateTimeField(auto_now_add=True)
    grievance_permission = models.CharField(max_length=50, default='Check')
    grievance_type = models.CharField(max_length=255, default='public')
    user = models.ForeignKey(WhiteBoardUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject + str(self.date_info)


class Placement(models.Model):

    stream = models.CharField(max_length=255)
    image_field = models.ImageField(blank=True, null=True)
    info = models.TextField()
    company = models.CharField(max_length=255)

    def __str__(self):
        return self.company + self.stream


class NewsFeed(models.Model):
    news_title = models.CharField(max_length=255)
    news_info = models.TextField()
    news_date = models.DateTimeField(auto_now_add=True)
    news_type = models.CharField(max_length=255, default="event")

    def __str__(self):
        return self.news_title + str(self.news_date)


class Assignments(models.Model):
    subject = models.CharField(max_length=255)
    stream = models.CharField(max_length=255)
    submission_date = models.DateTimeField(blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    info = models.TextField()

    def __str__(self):
        return self.subject + '_' + self.title


class StudentTest(models.Model):
    subject = models.CharField(max_length=255)
    stream = models.CharField(max_length=255)
    test_date = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=255)
    syllabus = models.TextField()

    def __str__(self):
        return self.subject + '_' + self.title