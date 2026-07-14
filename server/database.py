import mysql.connector
import sys
import os


sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)


from config.config import (
    DB_HOST,
    DB_USER,
    DB_PASSWORD,
    DB_NAME
)


def connect_db():

    db = mysql.connector.connect(

        host=DB_HOST,

        user=DB_USER,

        password=DB_PASSWORD,

        database=DB_NAME

    )

    return db



def register_user(email,password):

    db = connect_db()

    cursor = db.cursor()


    query = """

    INSERT INTO users(email,password,permission)

    VALUES(%s,%s,%s)

    """


    cursor.execute(

        query,

        (email,password,True)

    )


    db.commit()


    cursor.close()

    db.close()




def login_user(email,password):

    db = connect_db()

    cursor=db.cursor()


    query="""

    SELECT * FROM users

    WHERE email=%s AND password=%s

    """


    cursor.execute(

        query,

        (email,password)

    )


    result=cursor.fetchone()


    cursor.close()

    db.close()



    if result:

        return True

    else:

        return False
    
    
def save_file(filename, filepath, owner):

    db = connect_db()

    cursor = db.cursor()


    query = """
    INSERT INTO files(filename, filepath, owner)
    VALUES(%s,%s,%s)
    """


    cursor.execute(
        query,
        (
            filename,
            filepath,
            owner
        )
    )


    db.commit()


    cursor.close()
    db.close()

def get_files():

    db = connect_db()

    cursor = db.cursor()


    cursor.execute(
        "SELECT filename, filepath, owner, upload_time FROM files"
    )


    result = cursor.fetchall()


    cursor.close()

    db.close()


    return result


def save_media(filename, filepath, media_type, owner):


    db = connect_db()

    cursor = db.cursor()



    query = """

    INSERT INTO media(filename,filepath,type,owner)

    VALUES(%s,%s,%s,%s)

    """



    cursor.execute(

        query,

        (
            filename,
            filepath,
            media_type,
            owner
        )

    )


    db.commit()


    cursor.close()

    db.close()




def get_media():


    db = connect_db()

    cursor=db.cursor()



    cursor.execute(
        "SELECT * FROM media"
    )


    result=cursor.fetchall()



    cursor.close()

    db.close()



    return result