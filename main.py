from fastapi import FastAPI
import uvicorn

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World!"}


@app.get("/posts")
def get_posts():
    return {"data": "This is yout post"}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
