import requests

def get_mobile_number_location(api_key, mobile_number):
    url = "https://api.example.com/locate"
    params = {
        'apikey': api_key,
        'number': mobile_number
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return {
            'country': data.get('country'),
            'region': data.get('region'),
            'city': data.get('city'),
            'latitude': data.get('latitude'),
            'longitude': data.get('longitude'),
        }
    else:
        return None

# Example usage:
api_key = 'your_api_key'
mobile_number = '1234567890'
location = get_mobile_number_location(api_key, mobile_number)

if location:
    print(f"Location details for {mobile_number}:")
    print(f"Country: {location['country']}")
    print(f"Region: {location['region']}")
    print(f"City: {location['city']}")
    print(f"Latitude: {location['latitude']}")
    print(f"Longitude: {location['longitude']}")
else:
    print("Could not retrieve location information.")
