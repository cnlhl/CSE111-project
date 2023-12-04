-- For CSE 111 Code
CREATE DATABASE MeetMinder;

USE MeetMinder;

CREATE TABLE user (
    userid   INTEGER PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(99) NOT NULL,
    email    VARCHAR(99) NOT NULL,
    password VARCHAR(99) NOT NULL
);

CREATE TABLE meeting (
    meetingid   INTEGER PRIMARY KEY AUTO_INCREMENT,
    title       TEXT NOT NULL,
    description TEXT,
    time        DATE NOT NULL,
    location    TEXT NOT NULL,
    organizerid INTEGER NOT NULL,
    FOREIGN KEY (organizerid) 
        REFERENCES user(userid) 
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE agenda (
    agendaid INTEGER PRIMARY KEY AUTO_INCREMENT,
    topic    TEXT NOT NULL,
    duration INTEGER,
    meetingid INTEGER NOT NULL,
    FOREIGN KEY (meetingid) 
        REFERENCES meeting(meetingid) 
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE attendee (
    attendeeid INTEGER PRIMARY KEY AUTO_INCREMENT,
    userid     INTEGER NOT NULL,
    meetingid  INTEGER NOT NULL,
    status     TEXT NOT NULL,
    FOREIGN KEY (userid) 
        REFERENCES user(userid) 
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (meetingid) 
        REFERENCES meeting(meetingid) 
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE notification (
    notificationid INTEGER PRIMARY KEY AUTO_INCREMENT,
    userid         INTEGER NOT NULL,
    message        TEXT,
    timestamp      DATE NOT NULL,
    FOREIGN KEY (userid) 
        REFERENCES user(userid) 
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE room (
    roomid   INTEGER PRIMARY KEY AUTO_INCREMENT,
    name     TEXT NOT NULL,
    capacity INTEGER NOT NULL,
    resourceid INTEGER NOT NULL,
    FOREIGN KEY (resourceid) 
        REFERENCES resource(resourceid) 
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE resource (
    resourceid   INTEGER PRIMARY KEY AUTO_INCREMENT,
    resourcename TEXT NOT NULL,
    description  TEXT
);

CREATE TABLE meetingresource (
    meetingresourceid INTEGER PRIMARY KEY AUTO_INCREMENT,
    meetingid         INTEGER NOT NULL,
    resourceid        INTEGER NOT NULL,
    FOREIGN KEY (meetingid) 
        REFERENCES meeting(meetingid) 
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (resourceid) 
        REFERENCES resource(resourceid) 
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

SHOW TABLES;

DESCRIBE User;