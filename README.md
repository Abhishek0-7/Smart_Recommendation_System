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
  
## Additional Notes

1. **Dataset Preparation**: For the movies dataset, download the latest small dataset from MovieLens
                            For the books dataset, use the Goodbooks-10k dataset from GitHub

2. **Deployment Options**:

   - The current setup uses ngrok for temporary public access

   - For permanent deployment, consider services like:

    1. Heroku
    2. AWS Elastic Beanstalk
    3. Google App Engine

3. **Environment Variables**: Create a .env file for sensitive information:

       NGROK_AUTH_TOKEN=your_ngrok_token
       WEATHER_API_KEY=your_openweathermap_key
   
4. **Testing**: The test directory includes basic test cases
                Run tests with python -m pytest tests/

## 🤝 Contributing
Contributions are welcome! Please follow these steps:
1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.

## 📬 Contact
Email - abhishek261kumar@gmail.com  
Project Link: [https://github.com/Abhishek0-7/Smart_Recommendation_System](https://github.com/Abhishek0-7/Smart_Recommendation_System)
