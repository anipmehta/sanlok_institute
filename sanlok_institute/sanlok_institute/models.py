from django.db import models
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
class Marks(models.Model):
    score = models.FloatField(max_length=10, null=False)


@csrf_exempt
class Fees(models.Model):
    amount = models.FloatField(max_length=10, null=False)


@csrf_exempt
class Course(models.Model):
    id = models.CharField(max_length=50, null=False, primary_key=True)
    name = models.CharField(max_length=50, null=False)
    fees = models.OneToOneField(Fees, on_delete=models.CASCADE)


@csrf_exempt
class Timing(models.Model):
    slot = models.CharField(max_length=50, null=False)


@csrf_exempt
class Student(models.Model):
    enroll = models.CharField(max_length=10, null=False, primary_key=True)
    name = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length=10, null=False)
    email = models.CharField(max_length=100, null=True)
    course = models.ManyToManyField(Course, null=False)
    timing = models.ManyToManyField(Timing, null=False)
    marks = models.ForeignKey(Marks, null=True)


@csrf_exempt
class Inquiry(models.Model):
    name = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length=10, null=False)
    email = models.CharField(max_length=100, null=True)
    course = models.ManyToManyField(Course, null=False)
    timing = models.ManyToManyField(Timing, null=False)
