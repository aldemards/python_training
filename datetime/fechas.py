from datetime import datetime
from time import time

fecha_actual = datetime.now()
#print(fecha_actual)

fecha = datetime(2020,10,17)
#print(fecha)

fecha = datetime(2020,10,17,12,30,45)

#print(fecha)

fecha_formato = fecha.strftime('%d_%m_%Y %H:%M:%S')
#print(fecha_formato)

#print(fecha_actual.weekday()) # dia de la semana

fecha_formato = fecha_actual.strftime('%b-%d-%Y %H:%M:%S')
#print(fecha_formato)

#print(fecha_actual.strftime('%A %d %B %Y %H:%M %p'))


fecha_atentado = datetime(2001,9,11)
diferencia = fecha_actual - fecha_atentado

#print(diferencia)
#print(diferencia.days)
#print(diferencia.total_seconds())

import zoneinfo
from datetime import timezone
# pip install tzdata
# set() error

#for zone in zoneinfo.available_timezones():
#    print(zone)


#print(fecha_actual)
#print(datetime.now(timezone.utc))
print(datetime.now(timezone.utc).astimezone())
print(datetime.now(timezone.utc).astimezone(zoneinfo.ZoneInfo('America/New_York')))
print(datetime.now(timezone.utc).astimezone(zoneinfo.ZoneInfo('America/Los_Angeles')))