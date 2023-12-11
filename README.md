# MeetMinder
> A meeting scheduling system designed for modern professional businesses

Project by Haolin li &amp; Baixi Guo

## How to run

> This project is built with local backend and frontend. To run the project, you need to start both backend and frontend. But the MySQL database is hosted on Google Cloud, so you don't need to set up a local database.

1. Clone the project
2. Install dependencies
   1. vue3 frontend requires node.js and npm
   2. flask backend requires python3 and pip
3. Start backend
   1. `cd Back-end`
   3. `python3 app.py`
4. Start frontend
   1. `cd Front-end`
   2. `npm install`
   3. `npm run serve`

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