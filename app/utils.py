import datetime

def get_context_based_genres(weather=None):
    """Determine appropriate genres based on time of day, season, and weather"""
    now = datetime.datetime.now()
    hour = now.hour
    month = now.month
    
    # Time of day context
    if 5 <= hour < 12:  # Morning
        time_context = ["Animation", "Documentary", "Family"]
    elif 12 <= hour < 17:  # Afternoon
        time_context = ["Adventure", "Comedy", "Action"]
    elif 17 <= hour < 22:  # Evening
        time_context = ["Drama", "Romance", "Thriller"]
    else:  # Night
        time_context = ["Horror", "Thriller", "Mystery"]
    
    # Combine contexts
    combined_context = time_context
    return combined_context
