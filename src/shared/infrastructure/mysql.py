import mysql.connector

config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Darkrd3256*',
    'port': '3306',
    'database': 'calendario_flask',
}

DB = mysql.connector.connect(**config)
DB.autocommit = True
