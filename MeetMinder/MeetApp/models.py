from django.db import models


# User Table Model
class User(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=99)
    email = models.CharField(max_length=99)
    password = models.CharField(max_length=99)

    class Meta:
        managed = False
        db_table = 'user'
    
    def __str__(self):
        return f"User: {self.username}, Email: {self.email}"


# Meeting Table Model
class Meeting(models.Model):
    meetingid = models.AutoField(primary_key=True)
    title = models.TextField()
    description = models.TextField(blank=True, null=True)
    time = models.DateField()
    location = models.TextField()
    organizerid = models.ForeignKey('User', db_column='organizerid', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'meeting'
    
    def __str__(self):
        return f"Meeting: {self.title}, Description: {self.description}, Time: {self.time}, Location: {self.location}"


# Attendee Table Model
class Attendee(models.Model):
    attendeeid = models.AutoField(primary_key=True)
    userid = models.ForeignKey('User', db_column='userid', on_delete=models.CASCADE)
    meetingid = models.ForeignKey('Meeting', db_column='meetingid', on_delete=models.CASCADE)
    status = models.TextField()

    class Meta:
        managed = False
        db_table = 'attendee'

    def __str__(self):
        return f"Attendee Status: {self.status}"


# Notification Table Model
class Notification(models.Model):
    notificationid = models.AutoField(primary_key=True)
    userid = models.ForeignKey('User', db_column='userid', on_delete=models.CASCADE)
    message = models.TextField(blank=True, null=True)
    timestamp = models.DateField()

    class Meta:
        managed = False
        db_table = 'notification'
    
    def __str__(self):
        return f"Notification: {self.message}, Time Stamp: {self.timestamp}"


# Agenda Table Model
class Agenda(models.Model):
    agendaid = models.AutoField(primary_key=True)
    topic = models.TextField()
    duration = models.IntegerField(blank=True, null=True)
    meetingid = models.ForeignKey('Meeting', db_column='meetingid', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'agenda'

    def __str__(self):
        return f"Agenda: {self.topic}, Duration: {self.duration}"

# Resource Table Model
class Resource(models.Model):
    resourceid = models.AutoField(primary_key=True)
    resourcename = models.TextField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resource'
    
    def __str__(self):
        return f"Resource Description: {self.description}"


# Room Table Model
class Room(models.Model):
    roomid = models.AutoField(primary_key=True)
    name = models.TextField()
    capacity = models.IntegerField()
    resourceid = models.ForeignKey('Resource', db_column='resourceid', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'room'

    def __str__(self):
        return f"Room: {self.name}, Capacity: {self.capacity}"


# Meeting Resource Table Model
class Meetingresource(models.Model):
    meetingresourceid = models.AutoField(primary_key=True)
    meetingid = models.ForeignKey('Meeting', db_column='meetingid', on_delete=models.CASCADE)
    resourceid = models.ForeignKey('Resource', db_column='resourceid', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'meetingresource'
    
    def __str__(self):
        return "No Information Displayed!"


# Vote Table Model
class Votes(models.Model):
    vote_id = models.BigAutoField(primary_key=True)
    time_cast = models.DateTimeField()
    candidate = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'votes'
    
    def __str__(self):
        return "No Information Displayed!"