from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class GetSeason(BaseModel):
    number: int
    
def get_season(month: int) -> str:
    seasons = {
        1: "冬",
        2: "冬",
        3: "春",
        4: "春",
        5: "春",
        6: "夏",
        7: "夏",
        8: "夏",
        9: "秋",
        10: "秋",
        11: "秋",
        12: "冬",
    }

    #1~12以外の数字の場合はエラー
    if month < 1 or month > 12:
        raise HTTPException(status_code=400, detail="1から12の間の数字を入力してね！")

    return seasons[month]

@app.post("/get_season")
def get_season_api(month: GetSeason):
    season = get_season(month.number)
    return {f"{month}月は, {season}です！"}
