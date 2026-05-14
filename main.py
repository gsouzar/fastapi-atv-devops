from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API funcionando!", "ambiente": "ok"}

@app.get("/health")
def health():
    return {"status": "healthy"}