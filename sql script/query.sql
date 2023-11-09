-- 1. Insert a new user
INSERT INTO user (username, email, password) VALUES ('haolinli', 'haolin@example.com', 'password');

-- 2. Update a user's email
UPDATE user SET email = 'newemail@ucmerced.edu' WHERE userid = 21;

-- 3. Delete a user
DELETE FROM user WHERE userid = 21;

-- 4. Query all meetings for a specific user
SELECT * FROM meeting WHERE organizerid = 1;

-- 5. Insert a new meeting
INSERT INTO meeting (title, description, time, location, organizerid) VALUES ('Project presentation', 'pre for pj', '2023-11-10 10:00:00', 'library', 1);

-- 6. Update a meeting's description
UPDATE meeting SET description = 'New Meeting Description' WHERE meetingid = 21;

-- 7. Delete a meeting
DELETE FROM meeting WHERE meetingid = 21;

-- 8. Query all attendees for a specific meeting
SELECT * FROM attendee WHERE meetingid = 1;

-- 9. Insert a new agenda item for a meeting
INSERT INTO agenda (topic, duration, meetingid) VALUES ('Agenda Topic', 30, 1);

-- 10. Update an agenda item's duration
UPDATE agenda SET duration = 45 WHERE agendaid = 21;

-- 11. Delete an agenda item
DELETE FROM agenda WHERE agendaid = 21;

-- 12. Query all agenda items for a specific meeting
SELECT * FROM agenda WHERE meetingid = 1;

-- 13. Insert a new attendee for a meeting
INSERT INTO attendee (userid, meetingid, status) VALUES (1, 1, 'Attending');

-- 14. Update an attendee's status for a meeting
UPDATE attendee SET status = 'Not Attending' WHERE attendeeid = 21;

-- 15. Delete an attendee from a meeting
DELETE FROM attendee WHERE attendeeid = 21;

-- 16. Insert a new notification for a user
INSERT INTO notification (userid, message, timestamp) VALUES (1, 'Notification test Message', '2023-11-10 10:00:00');

-- 17. Update a notification's message for a user
UPDATE notification SET message = 'New Notification Message' WHERE notificationid = 21;

-- 18. Delete a notification for a user
DELETE FROM notification WHERE notificationid = 1;

-- 19. Query all notifications for a specific user
SELECT * FROM notification WHERE userid = 1;

-- 20. Insert a new room
INSERT INTO room (name, capacity, resourceid) VALUES ('Room Name', 10, 1);

-- 21. Update a room's capacity
UPDATE room SET capacity = 20 WHERE roomid = 21;

-- 22. Delete a room
DELETE FROM room WHERE roomid = 21;

-- 23. Query all resources for a specific room
SELECT * FROM resource WHERE resourceid IN (SELECT resourceid FROM room WHERE roomid = 1);

-- 24. Insert a new resource for a meeting
INSERT INTO meetingresource (meetingid, resourceid) VALUES (1, 1);

-- 25. Update a resource's description for a meeting
UPDATE resource SET description = 'New Resource Description' WHERE resourceid = 1;

-- 26. Delete a resource from a meeting
DELETE FROM meetingresource WHERE meetingresourceid = 1;

-- 27. Query all resources for a specific meeting
SELECT * FROM resource WHERE resourceid IN (SELECT resourceid FROM meetingresource WHERE meetingid = 1);

-- 28. Find all meetings that a user is attending
SELECT * FROM meeting WHERE meetingid IN (SELECT meetingid FROM attendee WHERE userid = 1);

-- 29. Find all meetings that a user is organizing
SELECT * FROM meeting WHERE organizerid = 1;

-- 30. Get all meetings organized by a specific user along with the agenda items for each meeting
SELECT user.username, meeting.title, agenda.topic
FROM user
JOIN meeting ON user.userid = meeting.organizerid
JOIN agenda ON meeting.meetingid = agenda.meetingid
WHERE user.username = 'user1';

-- 31. Get all attendees for all meetings organized by a specific user
SELECT user.username, meeting.title, attendee.userid
FROM user
JOIN meeting ON user.userid = meeting.organizerid
JOIN attendee ON meeting.meetingid = attendee.meetingid
WHERE user.username = 'user1';

-- 32. Get all resources for all meetings organized by a specific user
SELECT user.username, meeting.title, resource.resourcename
FROM user
JOIN meeting ON user.userid = meeting.organizerid
JOIN meetingresource ON meeting.meetingid = meetingresource.meetingid
JOIN resource ON meetingresource.resourceid = resource.resourceid
WHERE user.username = 'user1';

-- 33. Get the count of meetings each user has organized
SELECT user.username, COUNT(meeting.meetingid) AS meeting_count
FROM user
JOIN meeting ON user.userid = meeting.organizerid
GROUP BY user.username;

-- 34. Get the user who has organized the most meetings
SELECT user.username, COUNT(meeting.meetingid) AS meeting_count
FROM user
JOIN meeting ON user.userid = meeting.organizerid
GROUP BY user.username
ORDER BY meeting_count DESC
LIMIT 1;

-- 35. Get all users who have not organized any meetings
SELECT user.username
FROM user
LEFT JOIN meeting ON user.userid = meeting.organizerid
WHERE meeting.meetingid IS NULL;

-- 36. Get the average duration of all agenda items for each meeting
SELECT meeting.title, AVG(agenda.duration) AS average_duration
FROM meeting
JOIN agenda ON meeting.meetingid = agenda.meetingid
GROUP BY meeting.title;

-- 37. Get all meetings that have more than 3 agenda items
SELECT meeting.title
FROM meeting
JOIN agenda ON meeting.meetingid = agenda.meetingid
GROUP BY meeting.title
HAVING COUNT(agenda.agendaid) > 3;

-- 38. Get all meetings that have more than 3 attendees
SELECT meeting.title
FROM meeting
JOIN attendee ON meeting.meetingid = attendee.meetingid
GROUP BY meeting.title
HAVING COUNT(attendee.attendeeid) > 3;
