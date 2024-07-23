from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import FileResponse, JSONResponse
from views.board_view import upload_to_s3

router = APIRouter()

@router.get("/", response_class=FileResponse)
async def get_board():
    return FileResponse("./static/board.html", media_type="text/html")

@router.post("/submit-message")
async def submit_message(message: str = Form(...), file: UploadFile = File(...)):
    file_url = await upload_to_s3(file)
    return JSONResponse(content={"message": message, "file_url": file_url})