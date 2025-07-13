from pydantic import BaseModel, Field

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