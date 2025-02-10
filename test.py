import requests

def test_get_suggestions_with_city_name():
    url = "http://localhost:8000/suggestions"
    params = {
        "q": "London",
        "latitude": 43.70011, 
        "longitude": -79.4163 
    }
    response = requests.get(url, params=params, verify=False) 

    if response.status_code == 200:
        print("Response JSON:", response.json())
    else:
        print("Request failed with status code:", response.status_code)

test_get_suggestions_with_city_name()
