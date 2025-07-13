from fastapi import FastAPI, Response, exception_handlers
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from starlette.responses import Content
from schemas.memo import UpsertMemoSchema, MemoSchema, ResponseSchema

app = FastAPI()

@app.post("/memos", response_model=ResponseSchema)
async def create_memo(memo: UpsertMemoSchema):
    print(memo)
    return ResponseSchema(message="メモが正常に登録されました")

@app.get("/memos", response_model=list[MemoSchema])
async def get_memos_list():
    return [
        MemoSchema(title="タイトル1", description="詳細1", memo_id=1),
        MemoSchema(title="タイトル2", description="詳細2", memo_id=2),
        MemoSchema(title="タイトル3", description="詳細3", memo_id=3),
    ]

@app.get("/memos/{memo_id}", response_model=MemoSchema)
async def get_memo_detail(memo_id: int):
    return MemoSchema(title="タイトル1", description="詳細1", memo_id=memo_id)

@app.put("/memos/{memo_id}", response_model=ResponseSchema)
async def modify_memo(memo_id: int, memo: UpsertMemoSchema):
    print(memo_id, memo)
    return ResponseSchema(message="メモが正常に更新されました")

@app.delete("/memos/{memo_id}", response_model=ResponseSchema)
async def remove_memo(memo_id: int):
    print(memo_id)
    return ResponseSchema(message="メモが正常に削除されました")

@app.exception_handler(ValidationError)
async def validation_exception_handler(exc: ValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "detail": exc.errors()
        }
    )
