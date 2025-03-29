import pytest
from app import create_app
from unittest.mock import patch

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Smart Recommendation System" in response.data

def test_sentiment_analysis_route(client):
    test_data = {'text': 'I am feeling happy today!'}
    response = client.post('/analyze_sentiment', json=test_data)
    assert response.status_code == 200
    assert 'polarity' in response.json
    assert 'mood' in response.json

@patch('app.routes.RecommendationModels')
def test_movie_recommendation_route(mock_models, client):
    mock_models.return_value.movies_model.predict.return_value.est = 4.5
    mock_models.return_value.movies_data = {'userId': [1], 'movieId': [1], 'rating': [5], 'title': ['Test Movie']}
    
    response = client.get('/recommend/movies/1')
    assert response.status_code == 200
    assert isinstance(response.json, list)

@patch('app.routes.RecommendationModels')
def test_book_recommendation_route(mock_models, client):
    mock_models.return_value.books_model.predict.return_value.est = 4.5
    mock_models.return_value.books_data = {'user_id': [1], 'book_id': [1], 'rating': [5], 'title': ['Test Book']}
    
    response = client.get('/recommend/books/1')
    assert response.status_code == 200
    assert isinstance(response.json, list)

@patch('app.routes.requests.get')
def test_weather_route(mock_get, client):
    mock_response = {
        'main': {'temp': 20},
        'weather': [{'main': 'Clear', 'description': 'clear sky'}]
    }
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response
    
    response = client.get('/weather/london')
    assert response.status_code == 200
    assert 'temperature' in response.json
    assert 'weather' in response.json
