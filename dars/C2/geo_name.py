from geopy.geocoders import  Nominatim
def geo_location_name(latitude,longtitude):
    geolocator=Nominatim(user_agent='my_app')
    location=geolocator.reverse(f"{latitude} , {longtitude}")
    return location.address



# print(type(address))
# list_address=address.split(",")
# print(list_address)
# print(list_address[2])
