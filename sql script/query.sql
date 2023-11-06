-- 1. Insert a new user
INSERT INTO user (username, email, password) VALUES ('username', 'email@example.com', 'password');

-- 2. Update a user's email
UPDATE user SET email = 'newemail@example.com' WHERE userid = 1;

-- 3. Delete a user
DELETE FROM user WHERE userid = 1;

-- 4. Query all meetings for a specific user
SELECT * FROM meeting WHERE organizerid = 1;

-- 5. Insert a new meeting
INSERT INTO meeting (title, description, time, location, organizerid) VALUES ('Meeting Title', 'Meeting Description', '2022-01-01 10:00:00', 'Location', 1);

-- 6. Update a meeting's description
UPDATE meeting SET description = 'New Meeting Description' WHERE meetingid = 1;

-- 7. Delete a meeting
DELETE FROM meeting WHERE meetingid = 1;

-- 8. Query all attendees for a specific meeting
SELECT * FROM attendee WHERE meetingid = 1;

-- 9. Insert a new agenda item for a meeting
INSERT INTO agenda (topic, duration, meetingid) VALUES ('Agenda Topic', 30, 1);

-- 10. Update an agenda item's duration
UPDATE agenda SET duration = 45 WHERE agendaid = 1;

-- 11. Delete an agenda item
DELETE FROM agenda WHERE agendaid = 1;

-- 12. Query all agenda items for a specific meeting
SELECT * FROM agenda WHERE meetingid = 1;

-- 13. Insert a new attendee for a meeting
INSERT INTO attendee (userid, meetingid, status) VALUES (1, 1, 'Attending');

-- 14. Update an attendee's status for a meeting
UPDATE attendee SET status = 'Not Attending' WHERE attendeeid = 1;

-- 15. Delete an attendee from a meeting
DELETE FROM attendee WHERE attendeeid = 1;

-- 16. Insert a new notification for a user
INSERT INTO notification (userid, message, timestamp) VALUES (1, 'Notification Message', '2022-01-01 10:00:00');

-- 17. Update a notification's message for a user
UPDATE notification SET message = 'New Notification Message' WHERE notificationid = 1;

-- 18. Delete a notification for a user
DELETE FROM notification WHERE notificationid = 1;

-- 19. Query all notifications for a specific user
SELECT * FROM notification WHERE userid = 1;

-- 20. Insert a new room
INSERT INTO room (name, capacity, resourceid) VALUES ('Room Name', 10, 1);

-- 21. Update a room's capacity
UPDATE room SET capacity = 20 WHERE roomid = 1;

-- 22. Delete a room
DELETE FROM room WHERE roomid = 1;

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