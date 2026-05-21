# fastapiライブラリから FastAPI クラスを読み込む
from fastapi import FastAPI
# FastAPIの中の middleware フォルダの cors 機能から CORSMiddleware クラスを読み込む
from fastapi.middleware.cors import CORSMiddleware

# APIRouterを使って、APIのルーティングを定義
from fastapi import APIRouter
router = APIRouter(prefix="/api/hello", tags=["hello"])

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
    return {"message": "hello"}

# router登録
app.include_router(router)