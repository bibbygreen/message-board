from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import FileResponse, JSONResponse
from controllers.board_controller import message_submission, get_all_messages
from pathlib import Path

router = APIRouter()

@router.get("/board.html", response_class=FileResponse)
async def get_board():
    return FileResponse("./static/board.html", media_type="text/html")

@router.post("/api/submit-message")
async def handle_submit_message(username: str = Form(...), message: str = Form(...), file: UploadFile = File(...)):
    result = await message_submission(username, message, file)
    return JSONResponse(content=result)

@router.get("/api/messages")
async def fetch_messages():
    messages = await get_all_messages()
    formatted_messages = [
        {
            "username": msg[0],
            "message": msg[1],
            "file_url": msg[2]
        }
        for msg in messages
    ]
    return JSONResponse(content={"data": {"messages": formatted_messages}})

@router.get("/loaderio-784b0f7ef89615181f4a079f5395d350.txt")
async def get_loaderio_file():
    file_path = Path("static/loaderio-784b0f7ef89615181f4a079f5395d350.txt")
    if file_path.exists():
        return FileResponse(file_path, media_type="text/plain")
    return {"error": "File not found"}