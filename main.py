# FastAPI khởi động Javis
from fastapi import FastAPI
app = FastAPI()
@app.get('/')
def root():
    return {'message': 'UCIC Central Runtime is alive'}