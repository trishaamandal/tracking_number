import phonenumbers
from phonenumbers import geocoder
from num import number
import folium
Key = "32336379043a481cab115396c185593a" #api adress change by time  so first cheack the api adress
from phonenumbers import carrier 
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(Key)
