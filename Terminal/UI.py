from Controller import signinUser, countMeeting, nextMeetingTime, createMeeting, \
viewUser, viewMeeting, getUsername, updateAttendeeDecision, updateResource, viewResource, \
getCurrentMeetingID, createAttendee
from datetime import datetime

def get_hidden_input(prompt):
    password = ""
    print(prompt, end='', flush=True)
    while True:
        if char == '\r' or char == '\n':
            print('')
            break
        password += char
        print('*', end='', flush=True)
    return password

def get_user_input():
    username = input("Enter your username: ")
    password = input("Enter your password: ")  # Using getpass to hide the password input
    return username, password

def displayHomePageInfo(username, nextMeeting, meetingsToAttend):
    # Print Out Welcome Message
    print("*********************************************\n")
    print(f"Welcome to MeetMinder!\n")
    print("*********************************************\n")

    # Print User & Meeting Info
    print(f"Username: {username}")
    print(f"Current Time: {datetime.now()}")
    print(f"Next Meeting: {nextMeeting}")
    print(f"Meetings to Attend: {meetingsToAttend}")
    print()

def displayMenu():
    # Display Options
    print("Explore the following functionalities:")
    print("1. Create Meeting")
    print("2. View Meeting")
    print("3. Attendance to Meeting")
    print("4. Manage Resources")

def navigateThruMenu():
    chosen = False
    while not chosen:
        try:
            # Navigate Functionality Based On Options
            option = int(input("Choose Your Option: "))
            if option == 1:
                chosen = True
                return option
            elif option == 2:
                chosen = True
                return option
            elif option == 3:
                chosen = True
                return option
            elif option == 4:
                chosen = True
                return option
            else:
                print("Please enter a number between 1 to 4!")
        except ValueError:
            print("Please enter a valid input!")

def createMeetingOption(username):
    # Send Instruction
    print("\nTo create a meeting, you need to add following information:")
    print("Title, Decription, Time, Location")
    
    # Initialize Info
    finish = False
    meetingInput = []
    while not finish:
        # Wait for user input
        print("\nPlease fill out the information:")
        temp_title = input("Title: ")
        temp_description = input("Decription: ")
        temp_time = input("Time: ")
        temp_location = input("Location: ")

        res = input("Confirm your information? (Y/N): ")
        if(res.lower() == 'y'):
            # Fill in user input
            meetingInput.append(temp_title)
            meetingInput.append(temp_description)
            meetingInput.append(temp_time)
            meetingInput.append(temp_location)
            finish = True    

    # Create Meeting
    user = viewUser(username)
    userid = user[0]
    meetingInput.append(userid)
    createMeeting(meetingInput)

    # Create Attendee
    meetingid = getCurrentMeetingID()
    createAttendee([userid, meetingid, 'Attending'])

def viewMeetingOption(username):
    meetings = viewMeeting(username)
    if not meetings:
        print("You don't have meeting yet!")
        return None
    else:
        print("\nMeeting Details\n")
        for index, meeting in enumerate(meetings):
            print(f"Meeting {index + 1}:")
            print(f"Title: {meeting[1]}")
            print(f"Description: {meeting[2]}")
            print(f"DateTime: {meeting[3]}")
            print(f"Location: {meeting[4]}")
            organizerUsername = getUsername(meeting[5])
            print(f"Organizer: {organizerUsername}")
            print("*************************")
        return meetings
            
def MeetingAttendanceOption(username):
    # Get Meeting Data & User Data
    meetings = viewMeeting(username)
    user = viewUser(username)

    if not meetings:
        print("No meeting is available")
    else:
        # Get User ID
        userid = user[0]

        # Get Meeting ID
        meetingNum = int(input("Please choose meeting number (i.e. 1): "))
        meetingid = meetings[meetingNum-1][0]

        # Get User Decision
        print("Please choose the following decisions: ")
        decisionMade = False
        decisionWord = None
        while not decisionMade:
            decision = input("Attending(Y)/ Not Attending(N) / Maybe Attending(M): ")
            if decision.lower() == 'y':
                decisionWord = "Attending"
                decisionMade = True
            elif decision.lower() == 'n':
                decisionWord = "Not Attending"
                decisionMade = True
            elif decision.lower() == 'm':
                decisionWord = "Maybe Attending"
                decisionMade = True
            else:
                print("Please enter a valid decision")

        # Modify User Attendance
        updateAttendeeDecision(decisionWord, [userid, meetingid])

def viewResourceOption(userid, meetingid):
    resources = viewResource([userid, meetingid])

    if not resources:
        print("There is no resource for this meeting")
        return None
    else:
        print("\nResource Details\n")
        for index, resource in enumerate(resources):
            print(f"Resource {index + 1}:")
            print(f"Name: {resource[0]}")
            print(f"Description: {resource[1]}")
            print("*************************")
        return resources

def manageResourceOption(username):
    # Get Meeting Data User Data
    meetings = viewMeeting(username)
    user = viewUser(username)    

    if not meetings:
        print("No meeting is available")
    else:
        # Get User ID
        userid = user[0]

        # Get Meeting ID
        meetingNum = int(input("Please choose meeting number (i.e. 1): "))
        meetingid = meetings[meetingNum-1][0]

        # View Resource For Specific Meeting
        resources = viewResourceOption(userid, meetingid)
        if not resources:
            return None

        # Get Update Attribute
        print("Please choose one the following details to update: ")
        decisionMadeA = False
        updatedAttr = None
        while not decisionMadeA:
            choice = input("Resource Name(N)/ Resource Description(D): ")
            if choice.lower() == 'n':
                updatedAttr = 'resourcename'
                decisionMadeA = True
            elif choice.lower() == 'n':
                updatedAttr = "description"
                decisionMadeA = True
            else:
                print("Please enter a valid decision")

        # Get Update Value
        decisionMadeB = False
        updatedValue = None
        while not decisionMadeB:
            val = input("Please enter the value: ")
            if val:
                updatedValue = val
                decisionMadeB = True

        # Update Meeting Resource
        updateResource([updatedAttr, updatedValue, userid, meetingid])

# Main program
if __name__ == "__main__":
    try:
        authenticated = False
        # App starts here
        while not authenticated:
            # Users login
            username, password = get_user_input()
            authenticated = signinUser(username, password)

            # Navigate logged in users to home page
            if authenticated:
                # Display HomePage Info
                nextMeeting = nextMeetingTime(username)
                if not nextMeeting:
                    nextMeeting = "no meeting"
                meetingsToAttend = countMeeting(username)
                displayHomePageInfo(username, nextMeeting, meetingsToAttend)

                # Display & Choose Menu
                displayMenu()
                option = navigateThruMenu()
                if option == 1:
                    createMeetingOption(username)
                elif option == 2:
                    meetings = viewMeetingOption(username)
                elif option == 3:
                    MeetingAttendanceOption(username)
                elif option == 4:
                    manageResourceOption(username)
                else:
                    print("No Way You Escape That")

    except Exception as e:
        print(f"An error occurred: {e}")

    print()