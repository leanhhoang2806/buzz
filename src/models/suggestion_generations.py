from functools import lru_cache
from fuzzywuzzy import process
import pandas as pd
from geopy.distance import geodesic

class CityMatcher:
    df = pd.read_csv('src/models/cities_canada-usa.tsv', sep='\t')

    @staticmethod
    @lru_cache(maxsize=100) 
    def get_cached_top_matches(query, top_n=10):
        return process.extract(query, CityMatcher.df['name'].tolist(), limit=top_n)

    @staticmethod
    def calculate_final_score(query, lat=None, lon=None, top_n=10):
        top_matches = CityMatcher.get_cached_top_matches(query, top_n)
        final_scores = []
        
        for match in top_matches:
            city_name = match[0]
            score = match[1] / 100
            city_data = CityMatcher.df[CityMatcher.df['name'] == city_name].iloc[0]
            city_id = city_data['id']
            city_data = CityMatcher.df[CityMatcher.df['id'] == city_id].iloc[0]
            city_lat = city_data['lat']
            city_lon = city_data['long']
            
            if lat is not None and lon is not None:
                distance = geodesic((lat, lon), (city_lat, city_lon)).km
                final_score = score / (1 + distance / 100)
            else:
                final_score = score
            final_score = round(final_score, 2) 
            if final_score > 0.1:
                final_scores.append((city_data, final_score))
        
        final_scores.sort(key=lambda x: x[1], reverse=True)
        return final_scores
