from geocoder import geonames
from app.config import Config
from app.datastructures import Coordinates
from app.exceptions import CityNotFoundException


def get_city_coordinates(city_name: str) -> Coordinates:
    """Query the geo-service to find the city's latitude and longitude
    
    Raises: CityNotFoundException when the provided city is not found
    """
    try:
        city_data = geonames(city_name, key=Config.GEOCODER_API_KEY)
        if not city_data.ok:
            raise CityNotFoundException(
                message=f"The city {city_name} was not found. Please enter a valid city"
            )
        return Coordinates(lat=city_data.lat, lng=city_data.lng)
    except Exception: # TODO: BE MORE SPECIFIC!
        return Coordinates()
