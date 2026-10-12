from fastapi import FastAPI
app= FastAPI()

@app.get("/")
def home():
    return {"message": ["aditya","prashant ","kadam"]}

@app.get("/about")
def about():
    return {"message": ["my name is aditya kadam","i am a software engineer","i am a python developer"]}