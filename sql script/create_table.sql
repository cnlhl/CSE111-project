-- For CSE 111 Code
CREATE DATABASE meetminder;

USE meetminder;

CREATE TABLE user (
    userid   INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    email    VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    
    PRIMARY KEY (userid)
);

CREATE TABLE meeting (
    meetingid   INT NOT NULL AUTO_INCREMENT,
    title       VARCHAR(255) NOT NULL,
    description TEXT,
    time        DATETIME NOT NULL,
    location    VARCHAR(255) NOT NULL,
    organizerid INT NOT NULL,
    
    PRIMARY KEY (meetingid),
    FOREIGN KEY (organizerid) REFERENCES user(userid)
);

CREATE TABLE agenda (
    agendaid INT NOT NULL AUTO_INCREMENT,
    topic    VARCHAR(255) NOT NULL,
    duration INT,
    meetingid INT NOT NULL,
    
    PRIMARY KEY (agendaid),
    FOREIGN KEY (meetingid) REFERENCES meeting(meetingid)
);

CREATE TABLE attendee (
    attendeeid INT NOT NULL AUTO_INCREMENT,
    userid     INT NOT NULL,
    meetingid  INT NOT NULL,
    status     VARCHAR(255) NOT NULL,
    
    PRIMARY KEY (attendeeid),
    FOREIGN KEY (userid) REFERENCES user(userid),
    FOREIGN KEY (meetingid) REFERENCES meeting(meetingid)
);

CREATE TABLE notification (
    notificationid INT NOT NULL AUTO_INCREMENT,
    userid         INT NOT NULL,
    message        TEXT,
    timestamp      DATETIME NOT NULL,
    
    PRIMARY KEY (notificationid),
    FOREIGN KEY (userid) REFERENCES user(userid)
);

CREATE TABLE room (
    roomid   INT NOT NULL AUTO_INCREMENT,
    name     VARCHAR(255) NOT NULL,
    capacity INT NOT NULL,
    resourceid INT NOT NULL,
    
    PRIMARY KEY (roomid),
    FOREIGN KEY (resourceid) REFERENCES resource(resourceid)
);

CREATE TABLE resource (
    resourceid   INT NOT NULL AUTO_INCREMENT,
    resourcename VARCHAR(255) NOT NULL,
    description  TEXT,
    
    PRIMARY KEY (resourceid)
);

CREATE TABLE meetingresource (
    meetingresourceid INT NOT NULL AUTO_INCREMENT,
    meetingid         INT,
    resourceid        INT,
    
    PRIMARY KEY (meetingresourceid),
    FOREIGN KEY (meetingid) REFERENCES meeting(meetingid),
    FOREIGN KEY (resourceid) REFERENCES resource(resourceid)
);

SHOW TABLES;

DESCRIBE user;