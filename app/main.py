# fastapiライブラリから FastAPI クラスを読み込む
from fastapi import FastAPI
# FastAPIの中の middleware フォルダの cors 機能から CORSMiddleware クラスを読み込む
from fastapi.middleware.cors import CORSMiddleware
# api フォルダのhello.py から router を読み込む
from app.api import hello

# アプリ本体をを作成。appがWebアプリそのもの
app = FastAPI()

# 別のオリジン（URL）である「localhost:3000」からのアクセスを許可するように設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/hello")
def read_root():
    return {"message": "できた！"}

# router登録
app.include_router(hello.router)