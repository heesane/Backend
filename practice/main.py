from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
import logging
from datetime import datetime

from users import user

app = FastAPI()

logger = logging.getLogger("requests")

app.include_router(router=user.router,
                   prefix="/user"
                   )

@app.middleware("http")
async def log_requests(request: Request, call_next):
    # 요청 정보 추출
    method = request.method
    url = request.url
    client_ip = request.client.host
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 로그 메시지 생성
    log_message = f"[{timestamp}] IP: {client_ip} - Method: {method} - URL: {url}\n"

    # 로그 파일에 기록
    with open("log.txt", "a") as log_file:
        log_file.write(log_message)

    response = await call_next(request)
    return response

@app.get("/")
async def home():
    return FileResponse("index.html")