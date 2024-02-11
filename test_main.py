import pytest
from main import get_bike_share_count, app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_predict_route(client):
    """Test the predict route."""
    response = client.get('/predict')
    assert response.status_code == 200


def test_prediction(client):
    """Test the prediction functionality."""
    response = client.get('/predict?season=4&yr=0&holiday=0&atemp=0.457&casual=240&registered=2419')
    assert response.status_code == 200

    assert 2664 == eval(response.data)['bike_share']
