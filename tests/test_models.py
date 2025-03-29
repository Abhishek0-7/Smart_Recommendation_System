import pytest
from app.models import RecommendationModels
import pandas as pd

@pytest.fixture
def recommendation_models():
    models = RecommendationModels()
    models.load_data()
    models.train_models()
    return models

def test_data_loading(recommendation_models):
    assert recommendation_models.movies_data is not None
    assert recommendation_models.books_data is not None
    assert isinstance(recommendation_models.movies_data, pd.DataFrame)
    assert isinstance(recommendation_models.books_data, pd.DataFrame)

def test_model_training(recommendation_models):
    assert recommendation_models.movies_model is not None
    assert recommendation_models.books_model is not None
    assert hasattr(recommendation_models.movies_model, 'fit')
    assert hasattr(recommendation_models.books_model, 'fit')

def test_movies_data_columns(recommendation_models):
    required_columns = {'userId', 'movieId', 'rating', 'title', 'genres'}
    assert required_columns.issubset(recommendation_models.movies_data.columns)

def test_books_data_columns(recommendation_models):
    required_columns = {'user_id', 'book_id', 'rating', 'title'}
    assert required_columns.issubset(recommendation_models.books_data.columns)
