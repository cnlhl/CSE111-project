from django.db import models

class User(models.Model):
    username = models.CharField(max_length=99)
    email = models.CharField(max_length=99)
    password = models.CharField(max_length=99)

    def __str__(self):
        return self.username

class Meeting(models.Model):
    title = models.TextField()
    description = models.TextField(blank=True, null=True)
    time = models.DateField()
    location = models.TextField()
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_meetings')

    def __str__(self):
        return self.title

class Agenda(models.Model):
    topic = models.TextField()
    duration = models.IntegerField(null=True, blank=True)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, related_name='agendas')

    def __str__(self):
        return self.topic

class Attendee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attendances')
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, related_name='attendees')
    status = models.TextField()

    def __str__(self):
        return f"{self.user.username} attending {self.meeting.title}"

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField(blank=True, null=True)
    timestamp = models.DateField()

    def __str__(self):
        return f"Notification for {self.user.username}"

class Resource(models.Model):
    resourcename = models.TextField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.resourcename

class Room(models.Model):
    name = models.TextField()
    capacity = models.IntegerField()
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='rooms')

    def __str__(self):
        return self.name

class MeetingResource(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, related_name='meeting_resources')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='resource_meetings')

    def __str__(self):
        return f"{self.meeting.title} - {self.resource.resourcename}"
