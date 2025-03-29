import pandas as pd
from surprise import SVD, Dataset, Reader
from surprise.model_selection import train_test_split

class RecommendationModels:
    def __init__(self):
        self.movies_model = None
        self.books_model = None
        self.movies_data = None
        self.books_data = None
        
    def load_data(self):
        # Load movies data
        movies = pd.read_csv('data/movies/movies.csv')
        ratings = pd.read_csv('data/movies/ratings.csv')
        self.movies_data = pd.merge(ratings, movies, on='movieId')
        
        # Load books data
        self.books_data = pd.read_csv('data/books/books.csv')
        ratings_books = pd.read_csv('data/books/ratings.csv')
        self.books_data = pd.merge(ratings_books, self.books_data[['book_id', 'title']], 
                                 left_on='book_id', right_on='book_id')
    
    def train_models(self):
        # Train movies model
        reader = Reader(rating_scale=(0.5, 5.0))
        data_movies = Dataset.load_from_df(self.movies_data[['userId', 'movieId', 'rating']], reader)
        trainset, _ = train_test_split(data_movies, test_size=0.2)
        self.movies_model = SVD()
        self.movies_model.fit(trainset)
        
        # Train books model
        data_books = Dataset.load_from_df(self.books_data[['user_id', 'book_id', 'rating']], reader)
        trainset, _ = train_test_split(data_books, test_size=0.2)
        self.books_model = SVD()
        self.books_model.fit(trainset)
