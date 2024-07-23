from fastapi import UploadFile
from views.board_view import upload_to_s3

async def message_submission(message: str, file: UploadFile):
    file_url = await upload_to_s3(file)
    return {"message": message, "file_url": file_url}