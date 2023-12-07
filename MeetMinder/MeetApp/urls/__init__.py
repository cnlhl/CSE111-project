from django.urls import path, include
from MeetApp.urls import user_urls

urlpatterns = [
    path('user/', include(user_urls)),
    # path('meeting/', include(meeting_urls)),
]