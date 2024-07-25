from fastapi import UploadFile
from views.board_view import upload_to_s3
import mysql.connector
from database import get_db_connection

async def message_submission(username: str, message: str, file: UploadFile):
    file_url = await upload_to_s3(file)

    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            "INSERT INTO messages (username, content, file_url) VALUES (%s, %s, %s)",
            (username, message, file_url,)
        )
        connection.commit()
        message_submission_data = {
            "username": username, 
            "message": message, 
            "file_url": file_url
        }
        return message_submission_data

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return {"error": "Database error"}
    finally:
        cursor.close()
        connection.close()