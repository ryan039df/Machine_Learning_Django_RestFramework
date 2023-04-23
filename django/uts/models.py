from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

class Sensor2(models.Model):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

class Sensor3(models.Model):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

class Actuator(models.Model):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)