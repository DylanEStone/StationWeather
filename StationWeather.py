#!/usr/bin/python3

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

import config

owm = OWM(config.api_key)
mgr = owm.weather_manager()

# Goldstone
gObservation = mgr.weather_at_place('Goldstone, US')
g = gObservation.weather

print("\t***GOLDSTONE***")
print("Weather Status: " + g.detailed_status)
print(g.wind())
print("Cloud Coverage: " + str(g.clouds)+"\n\n")

# Canberra
cObservation = mgr.weather_at_place('Canberra, AU')
c = cObservation.weather

print("\t***CANBERRA***")
print("Weather Status: " + c.detailed_status)
print(c.wind())
print("Cloud Coverage: " + str(c.clouds) +"\n\n")

# Madrid
mObservation = mgr.weather_at_place('Madrid,ES')
m = mObservation.weather

print("\t***MADRID***")
print("Weather Status: " + m.detailed_status)
print(m.wind())
print("Cloud Coverage: " + str(m.clouds))
