CREATE TABLE user (
    userid   INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email    TEXT NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE meeting (
    meetingid   INTEGER PRIMARY KEY,
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
    agendaid INTEGER PRIMARY KEY,
    topic    TEXT NOT NULL,
    duration INTEGER,
    meetingid INTEGER NOT NULL,
    FOREIGN KEY (meetingid) 
        REFERENCES meeting(meetingid)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE attendee (
    attendeeid INTEGER PRIMARY KEY,
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
    notificationid INTEGER PRIMARY KEY,
    userid         INTEGER NOT NULL,
    message        TEXT,
    timestamp      DATE NOT NULL,
    FOREIGN KEY (userid) 
        REFERENCES user(userid)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE room (
    roomid   INTEGER PRIMARY KEY,
    name     TEXT NOT NULL,
    capacity INTEGER NOT NULL,
    resourceid INTEGER NOT NULL,
    FOREIGN KEY (resourceid) 
        REFERENCES resource(resourceid)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE resource (
    resourceid   INTEGER PRIMARY KEY,
    resourcename TEXT NOT NULL,
    description  TEXT
);

CREATE TABLE meetingresource (
    meetingresourceid INTEGER PRIMARY KEY,
    meetingid         INTEGER,
    resourceid        INTEGER,
    FOREIGN KEY (meetingid) 
        REFERENCES meeting(meetingid)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (resourceid) 
        REFERENCES resource(resourceid)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);