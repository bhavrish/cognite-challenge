import urllib.request
import numpy as np

site_url = "https://www.ndbc.noaa.gov/data/realtime2/KIKT.txt"
file = urllib.request.urlopen(site_url)

file_as_is = []
for line in file:
    decoded_line = line.decode("utf-8")
    #strip_content = decoded_line.split()
    #if (decoded_line )
    #print(decoded_line)
    file_as_is.append(decoded_line.split())

del file_as_is[:2] #removed first two rows (headers)
header = ["year", "month", "day", "hour", "minute", "WDIR_wind_direction","WSPD_wind_speed","GST_gust_speed","WVHT_wave_height","DPD_dominant_wave_period","APD_average_wave_period","MWD_wave_degree","PRES_sea_level_pressure","ATMP_air_temperature","WTMP_sea_surface_temperature","DEWP_dewpoint_temperature","VIS_station_visibility","PTDY_pressure_tendency","TIDE_water_level"]
file_as_is.insert(0,header) #adding in clean header

np.savetxt("KIKT.csv",file_as_is,delimiter=",",fmt='% s') #need to make dynamic
