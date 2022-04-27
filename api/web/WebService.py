from pyrebase import pyrebase
from psycopg2 import connect

# Works on Python 3.8.0
# For pyrebase install use: pip install pyrebase4
# pip version 22.0.4

firebaseConfig = {
    "apiKey": "AIzaSyDVdA0TB-zlPxdkzoh_Gxpynr_koHLWnGc",
    "authDomain": "miniprojectpythongame.firebaseapp.com",
    "projectId": "miniprojectpythongame",
    "storageBucket": "miniprojectpythongame.appspot.com",
    "messagingSenderId": "342094075809",
    "appId": "1:342094075809:web:6385d39bc01a7aad599de0",
    "measurementId": "G-397H9KP7RY",
    "databaseURL": ""
}

dbConfig = {
    'host': 'mini-projekt-game2-ptr-d137.aivencloud.com',
    'dbname': 'defaultdb',
    'user': 'avnadmin',
    'password': '1xGd6SHHC45Ym02Z',
    'port': '16578'
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


# returns reference to db connection (conn) and the cursor for db which can be used to perform actions in the db
def connect_to_db():
    conn, cursor = None, None
    try:
        conn = connect(
            host=dbConfig.get('host'),
            dbname=dbConfig.get('dbname'),
            user=dbConfig.get('user'),
            password=dbConfig.get('password'),
            port=dbConfig.get('port')
        )
        cursor = conn.cursor()

    except Exception as error:
        print(error)
    finally:
        return conn, cursor


def disconnect_from_db(conn, cursor):
    code = None
    try:
        cursor.close()
        conn.close()
        code = 0
    except Exception as error:
        print(error)
        code = 1
    finally:
        return code
