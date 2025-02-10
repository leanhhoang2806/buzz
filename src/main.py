from fastapi import FastAPI
from models.suggestion_generations import CityMatcher
from models.Suggestion import Suggestion


app = FastAPI()

@app.get("/health")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/suggestions")
def get_suggestions(q: str, latitude: float, longitude: float):
    top_matches = CityMatcher.calculate_final_score(q, latitude, longitude, 5)
    suggestions = []
    
    for city_data, final_score in top_matches:
        suggestions.append(Suggestion(
            name=f"{city_data['name']}, {city_data['country']}",
            latitude=city_data['lat'],
            longitude=city_data['long'],
            score=final_score
        ))
    
    return {"suggestions": suggestions}