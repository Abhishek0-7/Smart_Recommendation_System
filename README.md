# Smart_Recommendation_System
✨ Hybrid movie and book recommender using SVD + real-time context (mood/weather/time) with Flask/Surprise/TextBlob.

A context-aware recommendation system that provides personalized movie and book suggestions based on user preferences, current mood, time of day, and weather conditions.

**Features**

- **Personalized Recommendations**: Tailored suggestions based on user history
- **Sentiment Analysis**: Mood detection from user-provided text
- **Context Awareness**: Recommendations adapt to time, season, and weather
- **Multi-domain Recommendations**: Movies and books recommendations
- **Real-time Weather Integration**: Weather-based contextual suggestions

## Tech Stack

### Backend
- Python 3.8+
- Flask (Web Framework)
- Surprise (Recommendation Algorithms)
- Pandas (Data Processing)
- TextBlob (Sentiment Analysis)

### Frontend
- HTML5, CSS3, JavaScript
- Responsive Design

### Deployment
- Ngrok (Tunneling)
- Gunicorn (Production Server)

## Datasets

1. **Movies Dataset**: [MovieLens Latest Small](https://grouplens.org/datasets/movielens/latest/)
   - Contains 100,000 ratings from 1,000 users on 1,700 movies

2. **Books Dataset**: [Goodbooks-10k](https://github.com/zygmuntz/goodbooks-10k)
   - Contains 6 million ratings for 10,000 popular books
