from datetime import datetime
from pydantic import BaseModel, Field

class MemoStatusSchema(BaseModel):
    priority: str = Field(..., description="優先度", examples=["高"])
    due_date: datetime | None = Field(None,
                                      description="メモの期限日。設定がない場合はNone",
                                      examples=["2025-07-14T00:00:00"]
                                      )
    is_completed: bool = Field(False, description="メモが完了したかどうかを示すフラグ", examples=[False])

class UpsertMemoSchema(BaseModel):
    title: str = Field(...,
                       description="メモのタイトルを入力してください。少なくとも１文字以上必要です。",
                       examples=["明日のアジェンダ"],
                       min_length=1
                       )
    description: str = Field(default="",
                             description="メモの内容についての追加情報。任意で記入できます。",
                             examples=["会議で話すトピック：プロジェクトの進捗状況"]
                             )
    status: MemoStatusSchema = Field(..., description="メモの状態を表す情報")

class MemoSchema(UpsertMemoSchema):
    memo_id: int = Field(...,
                         description="メモを一意に識別するID番号。データベースで自動的に割り当てます。",
                         examples=[123]
                         )

class ResponseSchema(BaseModel):
    message: str = Field(...,
                         description="API操作の結果を説明するメッセージ。",
                         examples=["メモの更新に成功しました。"]
                         )