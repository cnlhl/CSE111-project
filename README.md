# MeetMinder
> A meeting scheduling system designed for modern professional businesses

Project by Haolin li &amp; Baixi Guo

## Basic User Case
### Organizer
1. Schedule Meeting
2. Create Meeting
3. Edit Meeting
4. Delete Meeting
### User
5. View Meeting
6. Attendance to Meeting
7. View Notifications
### System
8. Send Notification

## Relation Schema
- user(userid, username, email, password)
- meeting(meetingid, title, description, time, location, organizerid)
- agenda(agendaid, topic, duration, meetingid)
- attendee(attendeeid, userid, meetingid, status)
- notification(notificationid, userid, message, timestamp)
- room(roomid, name, capacity, resourceid)
- resource(resourceid, resourcename, description)
- meetingresource(meetingresourceid, meetingid, resourceid)

## Specific Operations
- [ ] 1. Insert a new user
- [ ] 2. Update a user's email
- [ ] 3. Delete a user
- [ ] 4. Query all meetings for a specific user
- [ ] 5. Insert a new meeting
- [ ] 6. Update a meeting's description
- [ ] 7. Delete a meeting
- [ ] 8. Query all attendees for a specific meeting
- [ ] 9. Insert a new agenda item for a meeting
- [ ] 10. Update an agenda item's duration
- [ ] 11. Delete an agenda item
- [ ] 12. Query all agenda items for a specific meeting
- [ ] 13. Insert a new attendee for a meeting
- [ ] 14. Update an attendee's status for a meeting
- [ ] 15. Delete an attendee from a meeting
- [ ] 16. Insert a new notification for a user
- [ ] 17. Update a notification's message for a user
- [ ] 18. Delete a notification for a user
- [ ] 19. Query all notifications for a specific user
- [ ] 20. Insert a new room
- [ ] 21. Update a room's capacity
- [ ] 22. Delete a room
- [ ] 23. Query all resources for a specific room
- [ ] 24. Insert a new resource for a meeting
- [ ] 25. Update a resource's description for a meeting
- [ ] 26. Delete a resource from a meeting
- [ ] 27. Query all resources for a specific meeting