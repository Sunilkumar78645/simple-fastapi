import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Hello, World'}

@app.get('/{name}')
def get_name(name: str):
    return {'Welcome ': f'{name}'}


@app.post('/trial')
def get_name(name: str):
    return {'Welcome ': f'{name}'}

if __name__ == '__main__':
    app.run()
    
# uvicorn app:app --reload
