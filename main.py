from typing import Optional


from fastapi import FastAPI, Path


app = FastAPI()


@app.get("/items/{item_id}/comments/{comment_id}")
async def read_comment(
    item_id: int = Path(...),
    comment_id: Optional[int] = None,
):
    if comment_id is None:
        return {"item_id": item_id}
    return {"item_id": item_id, "comment_id": comment_id}