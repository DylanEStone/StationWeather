from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps


owm = OWM('0dcfddcae5072808bdca1ec2fabb515f')
mgr = owm.weather_manager()

# Goldstone
gObservation = mgr.weather_at_place('Goldstone, US')
g = gObservation.weather

print("\tGoldstone")
print("Weather Status: " + g.detailed_status)
print(g.wind())
print(g.clouds)

# Canberra
cObservation = mgr.weather_at_place('Canberra, AU')
c = cObservation.weather

print("\tCanberra")
print("Weather Status: " + c.detailed_status)
print(c.wind())
print(c.clouds)

# Madrid
mObservation = mgr.weather_at_place('Madrid,ES')
m = mObservation.weather

print("\tMadrid")
print("Weather Status: " + m.detailed_status)
print(m.wind())
print(m.clouds)
