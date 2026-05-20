from fastapi import APIRouter

router = APIRouter(prefix="/api/hello", tags=["hello"])

# /api/helloにGETリクエストが来た場合の処理
@router.get("/api/hello")
def read_hello():
    return {"Hello World2"}