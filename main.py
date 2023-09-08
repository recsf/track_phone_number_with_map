import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import folium
from opencage.geocoder import OpenCageGeocode

number = input("Enter the phone number with country code: ")
phoneNumber = phonenumbers.parse(number)

Key = "11a812201ba34dca8d6f30823386029f"
geolocation = geocoder.description_for_number(phoneNumber, "en")
print("location: " + geolocation)

service = carrier.name_for_number(phoneNumber, "en")
print("service provider: " + service)

geocoder = OpenCageGeocode(Key)
query = str(geolocation)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=geolocation).add_to(myMap)

myMap.save("Location.html")
