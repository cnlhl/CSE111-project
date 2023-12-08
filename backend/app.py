from flask import Flask, request, jsonify
import pymysql
from flask_cors import CORS
from datetime import datetime
from email.utils import parsedate_to_datetime

app = Flask(__name__)
CORS(app)

current_user_id = None

# 数据库配置
db_config = {
    'host': '34.121.148.219',
    'port': 3306,  # 如果是默认端口可以省略
    'user': 'root',
    'password': 'meetminder',
    'db': 'meetminder',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

def get_db_connection():
    return pymysql.connect(**db_config)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']

    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT userid FROM user WHERE username = %s AND password = %s", (username, password))
            result = cursor.fetchone()

            if result:
                print('login success')
                global current_user_id
                current_user_id = result['userid']
                return jsonify({'success': True, 'userid': result['userid'], 'username': username})
            else:
                return jsonify({'success': False}), 401
    except pymysql.MySQLError as e:
        return jsonify({'error': str(e)}), 500
    finally:
        connection.close()

@app.route('/users', methods=['GET'])
def get_user_stats():
    userid = current_user_id
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            # 查询1: 获取应出席会议数量
            cursor.execute("SELECT COUNT(*) AS meetingsToAttend FROM attendee WHERE userid = %s AND status = 'Attending'", (userid,))
            result1 = cursor.fetchone()

            # 查询2: 获取下一次会议时间
            cursor.execute("SELECT MIN(time) AS nextMeeting FROM meeting JOIN attendee ON meeting.meetingid = attendee.meetingid WHERE userid = %s AND status = 'Attending'", (userid,))
            result2 = cursor.fetchone()

            # 查询3: 获取最新通知
            cursor.execute("SELECT message AS latestNotification FROM notification WHERE userid = %s ORDER BY timestamp DESC LIMIT 1", (userid,))
            result3 = cursor.fetchone()
            
            cursor.execute("SELECT username FROM user WHERE userid = %s", (userid,))
            result4 = cursor.fetchone()

            # 组合结果
            user_stats = {
                'meetingsToAttend': result1['meetingsToAttend'] if result1 else 0,
                'nextMeeting': result2['nextMeeting'] if result2['nextMeeting'] else 'no meeting',
                'latestNotification': result3['latestNotification'] if result3 else None,
                'username': result4['username'] if result4 else 'guest'
            }
            print(user_stats)
            return jsonify(user_stats)
    except pymysql.MySQLError as e:
        print(e)
        return jsonify({'error': str(e)}), 500
    finally:
        connection.close()

@app.route('/participants', methods=['GET'])
def get_participants():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM user")
            participants = cursor.fetchall()
            print(participants)
            return jsonify(participants)
    except pymysql.MySQLError as e:
        return jsonify({'error': str(e)}), 500
    finally:
        connection.close()
        
@app.route('/resources', methods=['GET'])
def get_resources():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM resource")
            resources = cursor.fetchall()
            return jsonify(resources)
    except pymysql.MySQLError as e:
        print(e)
        return jsonify({'error': str(e)}), 500
    finally:
        connection.close()

@app.route('/meetings', methods=['GET'])
def get_meetings():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT meeting.meetingid as meetingid,title, description, time, location,
                CASE 
                    WHEN attendee.userid = meeting.organizerid THEN 'Organizer'
                    ELSE 'Participant'
                END AS role
                FROM meeting 
                JOIN attendee ON meeting.meetingid = attendee.meetingid 
                WHERE attendee.userid = %s AND attendee.status = 'Attending'
            """, (current_user_id,))
            meetings = cursor.fetchall()
            print('find',current_user_id,meetings)
            return jsonify(meetings)
    except pymysql.MySQLError as e:
        print(e)
        return jsonify({'error': str(e)}), 500
    finally:
        connection.close()

@app.route('/meetings/pending', methods=['GET'])
def get_pending_meetings():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            # 执行 SQL 查询
            query = """
            SELECT meeting.meetingid as meetingid,title, description, time, location, 'pending' AS status
            FROM meeting
            JOIN attendee ON meeting.meetingid = attendee.meetingid
            WHERE attendee.status = 'Maybe Attending' and attendee.userid = %s
            """
            cursor.execute(query, (current_user_id,))
            meetings = cursor.fetchall()
            return jsonify(meetings)
    except pymysql.MySQLError as e:
        print(e)
        return jsonify({'error': str(e)}), 500
    finally:
        connection.close()

@app.route('/meetings', methods=['POST'])
def create_meeting():
    data = request.json
    title = data.get('title')
    description = data.get('description')
    time = data.get('time')
    location = data.get('location')
    participants = data.get('participants')  # 这是一个包含参与者信息的列表
    resources = data.get('resources')  # 这是一个包含资源信息的列表
        # ...前面的代码...

    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            # 插入新会议
            insert_meeting_sql = """
            INSERT INTO meeting (title, description, time, location, organizerid)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(insert_meeting_sql, (title, description, time, location, current_user_id))
            meeting_id = cursor.lastrowid  # 获取新插入的会议ID

            # 插入参与者记录到 attendee 表
            for participant in participants:
                insert_attendee_sql = """
                INSERT INTO attendee (meetingid, userid, status)
                VALUES (%s, %s, 'Maybe Attending')
                """
                cursor.execute(insert_attendee_sql, (meeting_id, participant['userid']))

            # 可以在这里插入相关的资源和通知操作
            for participant in participants:
                insert_notification_sql = """
                INSERT INTO notification (userid, message, timestamp)
                VALUES (%s, %s, NOW())
                """
                cursor.execute(insert_notification_sql, (participant['userid'], 'New meeting needs to be confirmed'))

            connection.commit()
            return jsonify({'success': True, 'meeting_id': meeting_id})
    except pymysql.MySQLError as e:
        connection.rollback()
        print(e)
        return jsonify({'error': str(e)}), 500
    finally:
        connection.close()
        
@app.route('/register', methods=['POST'])
def create_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            # 插入新用户
            insert_user_sql = """
            INSERT INTO user (username, password, email)
            VALUES (%s, %s, %s)
            """
            cursor.execute(insert_user_sql, (username, password,email))
            userid = cursor.lastrowid  # 获取新插入的用户ID

            connection.commit()
            return jsonify({'success': True, 'userid': userid})
    except pymysql.MySQLError as e:
        connection.rollback()
        print(e)
        return jsonify({'error': str(e)}), 500
    finally:
        connection.close()
        
@app.route('/updateattendance', methods=['POST'])
def update_attendance():
    data = request.json
    meetingid = data.get('meetingId')
    status = data.get('status')
    if status == 'attended':
        status = 'Attending'
    elif status == 'rejected':
        status = 'Not Attending'

    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            # 更新用户状态
            update_attendee_sql = """
            UPDATE attendee
            SET status = %s
            WHERE meetingid = %s AND userid = %s
            """
            cursor.execute(update_attendee_sql, (status, meetingid, current_user_id))
            print(status, meetingid, current_user_id)

            # 更新通知
            insert_notification_sql = """
            INSERT INTO notification (userid, message, timestamp)
            VALUES (%s, %s, NOW())
            """
            cursor.execute(insert_notification_sql, (current_user_id, 'Meeting status updated'))

            connection.commit()
            return jsonify({'success': True})
    except pymysql.MySQLError as e:
        connection.rollback()
        print(e)
        return jsonify({'error': str(e)}), 500
    finally:
        connection.close()
        
@app.route('/updateresources', methods=['PUT'])
def updateresources():
    data = request.json
    # {'description': 'New Description', 'resourceid': 1, 'resourcename': 'resource1', 'editing': True}     
    description = data.get('description')
    resourceid = data.get('resourceid')
    resourcename = data.get('resourcename')
    roomid = data.get('roomid')
    
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            update_resource_sql = """
                UPDATE resource
                SET description = %s, resourcename = %s
                WHERE resourceid = %s
            """
            cursor.execute(update_resource_sql, (description, resourcename, resourceid))
            print(description, resourcename, resourceid)
            if roomid is not None:
                update_resource_sql = """
                    UPDATE room
                    SET name = %s,capacity = %s
                    WHERE roomid = %s
                """
                cursor.execute(update_resource_sql, (data.get('roomname'), data.get('capacity'), roomid))
                print(roomid, resourceid)
            connection.commit()
            return jsonify({'success': True})
    except pymysql.MySQLError as e:
        connection.rollback()
        print(e)
        return jsonify({'error': str(e)}), 500
    finally:
        connection.close()

@app.route('/deleteresources/<int:resource_id>', methods=['DELETE'])
def deleteresources(resource_id):
    print(resource_id)
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            # 删除资源
            delete_resource_sql = """
            DELETE FROM resource
            WHERE resourceid = %s
            """
            cursor.execute(delete_resource_sql, (resource_id))
            print(resource_id)

            connection.commit()
            return jsonify({'success': True})
    except pymysql.MySQLError as e:
        connection.rollback()
        print(e)
        return jsonify({'error': str(e)}), 500
    finally:
        connection.close()

@app.route('/rooms', methods=['get'])
def get_rooms():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM room")
            rooms = cursor.fetchall()
            return jsonify(rooms)
    except pymysql.MySQLError as e:
        print(e)
        return jsonify({'error': str(e)}), 500
    finally:
        connection.close()
        
@app.route('/updatemeetings', methods=['POST'])
def updatemeetings():
    data = request.json
    #  [{'meetingid': 42, 'title': 'test', 'description': 'test', 'time': datetime.datetime(2023, 12, 1, 12, 12), 'location': 'west', 'Role': 'Organizer'}, {'meetingid': 43, 'title': "111's orientation", 'description': 'welcome', 'time': datetime.datetime(2023, 12, 22, 12, 13), 'location': 'library', 'Role': 'Participant'}]
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            for meeting in data:
                time = parsedate_to_datetime(meeting['time'])
                update_meeting_sql = """
                    UPDATE meeting
                    SET title = %s, description = %s, time = %s, location = %s
                    WHERE meetingid = %s
                """
                cursor.execute(update_meeting_sql, (meeting['title'], meeting['description'],  time, meeting['location'], meeting['meetingid']))
                print(meeting['title'], meeting['description'], time, meeting['location'], meeting['meetingid'])
            connection.commit()
            return jsonify({'success': True})
    except pymysql.MySQLError as e:
        connection.rollback()
        print(e)
        return jsonify({'error': str(e)}), 500
    finally:
        connection.close()
        
@app.route('/deletemeetings', methods=['POST'])
def deletemeetings():
    data = request.json
    meeting_id = data.get('meetingid')
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            # 删除会议
            delete_meeting_sql = """
            DELETE FROM meeting
            WHERE meetingid = %s
            """
            cursor.execute(delete_meeting_sql, (meeting_id))
            print(meeting_id)

            connection.commit()
            return jsonify({'success': True})
    except pymysql.MySQLError as e:
        connection.rollback()
        print(e)
        return jsonify({'error': str(e)}), 500
    finally:
        connection.close()

if __name__ == '__main__':
    app.run(debug=True)
