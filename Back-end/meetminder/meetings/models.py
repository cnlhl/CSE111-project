from django.db import models

class User(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=99, unique=True)
    email = models.EmailField(max_length=99, unique=True)
    password = models.CharField(max_length=99)

    class Meta:
        db_table = 'user'

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
        return f'{self.user.username} - {self.meeting.title}'

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField(blank=True, null=True)
    timestamp = models.DateField()

    def __str__(self):
        return f'Notification for {self.user.username} on {self.timestamp}'

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
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, related_name='resources')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='meetings')

    def __str__(self):
        return f'Resource {self.resource.resourcename} for meeting {self.meeting.title}'
