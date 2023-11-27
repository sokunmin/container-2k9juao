from datetime import datetime
from fastapi import FastAPI, Request

app = FastAPI()
@app.post("/api/test")
async def receive_data(request: Request):
    data = await request.json()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print('server.receive=', data)
    return {"message": now, "success": True}
