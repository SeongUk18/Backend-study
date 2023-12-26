from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi import Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

class Post(BaseModel):
    title: str
    content: str

posts: List[Post] = []


@app.get("/", response_class=HTMLResponse)
def read_root():
    with open('static/index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

@app.post("/create_post")
def create_post_from_form(title: str = Form(...), content: str = Form(...)):
    post = Post(title=title, content=content)
    posts.append(post)
    return {"message": "Post created successfully", "post_id": len(posts) - 1}

@app.get("/posts/")
def get_posts():
    return posts

@app.get("/posts/{post_id}")
def get_post(post_id: int):
    return posts[post_id]

@app.get("/posts/{post_id}")
def get_post(post_id: int):
    return posts[post_id]

@app.put("/posts/{post_id}")
def update_post(post_id: int, post: Post):
    posts[post_id] = post
    return {"message": "Post updated successfully"}

@app.delete("/posts/{post_id}")
def delete_post(post_id: int):
    posts.pop(post_id)
    return {"message": "Post deleted successfully"}
