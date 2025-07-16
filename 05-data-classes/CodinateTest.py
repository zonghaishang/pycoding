from Cordinate import Cordinate

moscow = Cordinate(55.76, 37.62)
print(moscow)

location = Cordinate(55.76, 37.62)
print("moscow == location", moscow == location)

print("(moscow.lat, moscow.lon) == (location.lat, location.lon)"
      , (moscow.lat, moscow.lon) == (location.lat, location.lon))
