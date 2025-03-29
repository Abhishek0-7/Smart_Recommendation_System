from flask import Blueprint, jsonify, request, render_template
from .models import RecommendationModels
from textblob import TextBlob
import datetime
import requests
import os

main = Blueprint('main', __name__)
models = RecommendationModels()
models.load_data()
models.train_models()

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    data = request.json
    text = data.get('text', '')
    sentiment = TextBlob(text).sentiment
    return jsonify({
        'polarity': sentiment.polarity,
        'subjectivity': sentiment.subjectivity,
        'mood': 'positive' if sentiment.polarity > 0.2 else 'negative' if sentiment.polarity < -0.2 else 'neutral'
    })

@main.route('/recommend/movies/<int:user_id>')
def recommend_movies(user_id):
    # Implementation similar to your original code
    pass

@main.route('/recommend/books/<int:user_id>')
def recommend_books(user_id):
    # Implementation similar to your original code
    pass

@main.route('/weather/<city>')
def get_weather(city):
    # Implementation similar to your original code
    pass
