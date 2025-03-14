from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_retorna_ola_mundo():
    client = TestClient(app) # Arrange

    response = client.get('/') # Act

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'} # Assert
