import mysql.connector

credential = {
    "host": "34.121.148.219",
    "user": "root",
    "password": "meetminder",
    "database": "meetminder",
}

def MySQLConnect():
    connection = mysql.connector.connect(
        host=credential["host"],
        user=credential["user"],
        password=credential["password"],
        database=credential["database"]
    )
    return connection