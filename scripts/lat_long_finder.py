from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable

def get_location_coordinates(location):
    geolocator = Nominatim(user_agent="my_app")
    
    # Specify the country code for Timor Leste
    country_code = "TL"
    
    # Construct the query string with the location and country code
    query = f"{location}, {country_code}"
    
    try:
        # Geocode the location
        location_data = geolocator.geocode(query)
        
        if location_data:
            latitude = location_data.latitude
            longitude = location_data.longitude
            return latitude, longitude
        else:
            return None, None
    except GeocoderUnavailable as e:
        print(f"Geocoding service is unavailable. Error: {str(e)}")
        return None, None

# Example usage
location_name = input("Enter a location name in Timor Leste: ")
latitude, longitude = get_location_coordinates(location_name)

if latitude and longitude:
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
else:
    print("Location not found or geocoding service unavailable.")