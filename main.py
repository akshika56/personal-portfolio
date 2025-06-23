import phonenumbers
from phonenumbers import geocoder
#from test import number
import folium

key = "67bb1d6360ab45dcb2919c439f186f09"

number=input("Enter your number with country code:")

#Parses the number to validate and prepare it for extracting metadata.
check_number = phonenumbers.parse(number)
#Returns a textual location such as "India" or "California" depending on the number.
number_location = geocoder.description_for_number(check_number,"en")
print(number_location)


from phonenumbers import carrier
service_provider = phonenumbers.parse(number)

#Returns the carrier name, like "Airtel" or "AT&T".
print(carrier.name_for_number(service_provider,"en"))

from opencage.geocoder import OpenCageGeocode
#Uses the number_location (like "India") as a query to OpenCage API to get coordinates.
geocoder = OpenCageGeocode(key)

query = str(number_location)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

#Creates an interactive map centered at the detected location.
#Adds a marker with a popup label.
map_location = folium.Map(location = [lat,lng], zoom_start=9)
folium.Marker([lat,lng], popup=number_location).add_to(map_location)
map_location.save("mylocation.html")