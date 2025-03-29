import os

class Config:
    # API Keys
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "your_api_key_here")  # From environment variables
    
    # Model Parameters
    SVD_N_FACTORS = 100           # Latent factors for SVD
    SVD_N_EPOCHS = 20            # Training iterations
    TOP_K_RECOMMENDATIONS = 5     # Number of suggestions
    
    # Paths
    MOVIES_DATA_PATH = "data/movies/"
    BOOKS_DATA_PATH = "data/books/"
