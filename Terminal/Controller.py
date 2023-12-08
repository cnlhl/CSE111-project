import mysql.connector
from Config import MySQLConnect

def signinUser(username, password):
    # Input Argument Sample: ("user3", "password3")
    # Input Type (string, string)

    connection = MySQLConnect()
    
    try:
        if connection.is_connected():
            # print(f"Connected to the MySQL database")

            cursor = connection.cursor()

            query = "SELECT password FROM user WHERE username=%s"
            param = (username,)
            cursor.execute(query, param)
            pw = cursor.fetchone()

            if not pw:
                print('\nUsername not found, try again!\n')
                return False
            else:
                if pw[0] == password:
                    print('\nUser Authenticated!\n')
                    authenticated = True
                else:
                    print('\nPassword not valid, try again!\n')
                    authenticated = False
                return authenticated
        else:
            print("\nConnection failed!\n")
            return False
    finally:
        connection.close()

def viewUser(username):
    # Input Argument Sample: ("user3")
    # Input Type: (String)

    connection = MySQLConnect()

    try:
        if connection.is_connected():
            # print(f"Connected to the MySQL database")

            cursor = connection.cursor()

            query = "SELECT * FROM user WHERE username=%s"
            param = (username,)
            cursor.execute(query, param)
            userInfo = cursor.fetchone()

            if userInfo:
                # print("Fetch User Info Successfully")
                return list(userInfo)
            else:
                return None

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        connection.close()

def getUsername(ID):
    # Input Argument Sample: (11)
    # Input Type: (int)

    connection = MySQLConnect()

    try:
        if connection.is_connected():
            # print(f"Connected to the MySQL database")

            cursor = connection.cursor()

            query = "SELECT username FROM user WHERE userid=%s"
            param = (ID,)
            cursor.execute(query, param)
            username = cursor.fetchone()

            if username:
                # print("Fetch Username Successfully")
                return list(username)[0]
            else:
                return None

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        connection.close()

def createMeeting(meetingInput):
    # Input Argument Sample: (("Capstone Meeting", "No Comment", "2023-12-07", "Merced", 3))
    # Input Type (Tuple(string, string, string, string, int))

    connection = MySQLConnect()

    try:
        if connection.is_connected():
            # print(f"Connected to the MySQL database")

            cursor = connection.cursor()

            query = "INSERT INTO meeting(title, description, time, location, organizerid) \
                     VALUES(%s, %s, %s, %s, %s)"
            param = meetingInput
            cursor.execute(query, param)

            connection.commit()
            print("New entry inserted successfully")
        else:
            print("Connection failed")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        connection.close()

def viewMeeting(username):
    # Input Argument Sample: ("user1")
    # Input Type: (string)

    connection = MySQLConnect()

    try:
        if connection.is_connected():
            # print(f"Connected to the MySQL database")

            cursor = connection.cursor()

            query = "SELECT meeting.meetingid, title, description, time, location, organizerid  \
                     FROM user, attendee, meeting \
                     WHERE user.userid = attendee.userid AND attendee.meetingid = meeting.meetingid AND \
                     user.username = %s"
            param = (username, )
            cursor.execute(query, param)
            meetingInfo = cursor.fetchall()

            if(meetingInfo):
                # print("Find Relevant Meeting Successfully")
                return meetingInfo
            else:
                return None
        else:
            print("Connection failed")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        connection.close()

def updateMeeting(updateInput):
    # Input Argument Sample: (["location", "Los Angeles", 1])
    # Input Type: (List(string, string, int))

    connection = MySQLConnect()

    try:
        if connection.is_connected():
            print(f"Connected to the MySQL database")

            cursor = connection.cursor()

            query = f"UPDATE meeting SET {updateInput[0]}=%s WHERE meetingid=%s"
            param = (updateInput[1], updateInput[2])
            cursor.execute(query, param)

            connection.commit()
            print("Update Meeting Successfully")
        else:
            print("Connection failed")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        connection.close()

def countMeeting(username):
    # Input Argument Sample: ("user4")
    # Input Type: (string)

    connection = MySQLConnect()

    try:
        if connection.is_connected():
            # print(f"Connected to the MySQL database")

            cursor = connection.cursor()

            query = "SELECT COUNT(*) \
                     FROM user, attendee, meeting \
                     WHERE user.userid = attendee.userid AND attendee.meetingid = meeting.meetingid AND \
                     user.username = %s"
            param = (username, )
            cursor.execute(query, param)
            count = cursor.fetchone()

            # print("Calculate Meeting Count Successfully")
            return count[0]
        else:
            print("Connection failed")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        connection.close()

def nextMeetingTime(username):
    # Input Argument Sample: ("user4")
    # Input Type: (string)

    connection = MySQLConnect()

    try:
        if connection.is_connected():
            # print(f"Connected to the MySQL database")

            cursor = connection.cursor()

            query = "SELECT time \
                    FROM user, attendee, meeting \
                    WHERE user.userid = attendee.userid AND attendee.meetingid = meeting.meetingid AND \
                    user.username = %s \
                    ORDER BY time ASC \
                    LIMIT 1"
            param = (username, )
            cursor.execute(query, param)
            nextTime = cursor.fetchone()
            
            if nextTime:
                # print("Find Next Meeting Time Successfully")
                return nextTime[0]
            else:
                return None
                
        else:
            print("Connection failed")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        connection.close()

def getCurrentMeetingID():
    connection = MySQLConnect()

    try:
        if connection.is_connected():
            # print(f"Connected to the MySQL database")

            cursor = connection.cursor()

            query = "SELECT MAX(meetingid) FROM meeting"
            cursor.execute(query)
            meetingid = cursor.fetchone()

    
            print("Get Current MeetingID Successfully")
            return meetingid[0]
        else:
            print("Connection failed")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        connection.close()

def createAttendee(attendeeInput):
    # Input Argument Sample: ([11, 33])
    # Input Type: (List(int, int))
    
    connection = MySQLConnect()

    try:
        if connection.is_connected():
            # print(f"Connected to the MySQL database")

            cursor = connection.cursor()

            query = "INSERT INTO attendee(userid, meetingid, status)\
                     VALUES(%s, %s, %s)"
            param = (attendeeInput[0], attendeeInput[1], attendeeInput[2])
            cursor.execute(query, param)

            connection.commit()
            print("Create Attendee Successfully")
        else:
            print("Connection failed")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        connection.close()

def updateAttendeeDecision(decision, attendeeInput):
    # Input Argument Sample: ("Attending", [11, 33])
    # Input Type: (string, List(int, int))
    
    connection = MySQLConnect()

    try:
        if connection.is_connected():
            print(f"Connected to the MySQL database")

            cursor = connection.cursor()

            query = "UPDATE attendee \
                     SET status= %s \
                     WHERE userid = %s AND meetingid = %s"
            param = (decision, attendeeInput[0], attendeeInput[1])
            cursor.execute(query, param)

            connection.commit()
            print("Update Attendee Status Successfully")
        else:
            print("Connection failed")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        connection.close()

def viewResource(resourceInput):
    # Input Argument Sample: ([15,1])
    # Input Type: (List(int, int))

    connection = MySQLConnect()

    try:
        if connection.is_connected():
            print(f"Connected to the MySQL database")

            cursor = connection.cursor()

            query = "SELECT resource.resourcename, resource.description  \
                     FROM user, meeting, meetingresource, resource \
                     WHERE \
                        user.userid = meeting.organizerid AND \
                        meeting.meetingid = meetingresource.meetingid AND \
                        meetingresource.resourceid = resource.resourceid AND \
                        user.userid = %s AND meeting.meetingid = %s"
            param = (resourceInput[0], resourceInput[1])
            cursor.execute(query, param)
            resourceInfo = cursor.fetchall()

            if resourceInfo:
                print("Fetch Resource Info Successfully")
                return resourceInfo
            else:
                return None
        else:
            print("Connection failed")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        connection.close()

def updateResource(resourceInput):
    # Input Argument Sample: (["description", "No Description", 15, 1])
    # Input Type: (List(string, *Depends On First Element, int, int))

    connection = MySQLConnect()

    try:
        if connection.is_connected():
            print(f"Connected to the MySQL database")

            cursor = connection.cursor()

            query = f"UPDATE \
                        user \
                        JOIN meeting ON user.userid = meeting.organizerid \
                        JOIN meetingresource ON meeting.meetingid = meetingresource.meetingid \
                        JOIN resource ON meetingresource.resourceid = resource.resourceid \
                      SET resource.{resourceInput[0]}=%s \
                      WHERE user.userid = %s AND meeting.meetingid = %s"
            param = (resourceInput[1], resourceInput[2], resourceInput[3])
            cursor.execute(query, param)
            connection.commit()
            print("Update Meeting Successfully")
        else:
            print("Connection failed")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        connection.close()

def viewNotification(username):
    # Input Argument Sample: ("user11")
    # Input Type: (string)

    connection = MySQLConnect()

    try:
        if connection.is_connected():
            print(f"Connected to the MySQL database")

            cursor = connection.cursor()

            query = "SELECT * \
                     FROM user JOIN notification ON user.userid = notification.userid \
                     WHERE user.username = %s"
            param = (username, )
            cursor.execute(query, param)
            resourceInfo = cursor.fetchall()
            
            if(resourceInfo):
                print("Fetch Notification Info Successfully")
                return resourceInfo
            else:
                return None
        else:
            print("Connection failed")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        connection.close()

if __name__ == "__main__":
    # SignIn = signinUser("user3", "password3")
    # print(SignIn)w

    # userInfo = viewUser('user11')
    # print(userInfo)

    # createMeeting(("Capstone Meeting", "No Comment", "2023-12-07", "Merced", 3))

    # count = countMeeting("user40")
    # print(count)

    #  nextTime = nextMeetingTime("user11")
    #  print(nextTime)

    # meetingInfo = viewMeeting("user11")
    # print(meetingInfo)

    # updateMeeting(["location", "Los Angeles", 1])

    # updateAttendeeDecision("Attending", [11, 33])

    # resourceInfo = viewResource([15,1])
    # print(resourceInfo)

    # updateResource(["description", "New Description", 15, 1])

    # notificationInfo = viewNotification("user400")
    # print(notificationInfo)

    # username = getUsername(11)
    # print(username) 

    id = getCurrentMeetingID()
    print(id)

    createAttendee([1,id])