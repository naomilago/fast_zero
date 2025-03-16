from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.get('/html', status_code=HTTPStatus.OK)
def read_html():
    style = """
        <style>
            h1 {
                font-size: 32pt;
                color: teal;
                text-align: center;
                margin-top: 50px;
            }
        </style>
    """

    return HTMLResponse(f'{style}<h1>Olá Mundo!</h1>')
