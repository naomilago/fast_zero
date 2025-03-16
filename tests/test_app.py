from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_retorna_ola_mundo():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert


def test_html_retorna_ola_mundo_em_html():
    client = TestClient(app)

    response = client.get('/html')

    assert response.status_code == HTTPStatus.OK
    assert '<h1>Olá Mundo!</h1>' in response.text
