import pyowm

owm = pyowm.OWM('ad6916161bbca20f1129a7f1d8fdc06c')
observation = owm.weather_at_place('Ghana,Cape Coast')
w = observation.get_weather()

w.get_wind()
w.get_humidity()
w.get_tempreture

print (w.get_wind())
print (w.get_humidity())
