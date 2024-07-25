from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import FileResponse, JSONResponse
from views.board_view import upload_to_s3
from controllers.board_controller import message_submission

router = APIRouter()

@router.get("/", response_class=FileResponse)
async def get_board():
    return FileResponse("./static/board.html", media_type="text/html")

@router.post("/submit-message")
async def handle_submit_message(username: str = Form(...), message: str = Form(...), file: UploadFile = File(...)):
    result = await message_submission(username, message, file)
    return JSONResponse(content=result)