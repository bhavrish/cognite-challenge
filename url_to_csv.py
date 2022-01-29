import urllib.request
import re
import numpy as np

'''
    input: list of list
    output: flattened list
    ref: https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-a-list-of-lists
'''
def flatten(data):
    return [item for sublist in data for item in sublist]

source_urls = ["https://www.ndbc.noaa.gov/data/realtime2/KIKT.txt","https://www.ndbc.noaa.gov/data/realtime2/KBQX.txt","https://www.ndbc.noaa.gov/data/realtime2/KMIS.txt"]
header = ["year", "month", "day", "hour", "minute", "WDIR_wind_direction","WSPD_wind_speed","GST_gust_speed","WVHT_wave_height","DPD_dominant_wave_period","APD_average_wave_period","MWD_wave_degree","PRES_sea_level_pressure","ATMP_air_temperature","WTMP_sea_surface_temperature","DEWP_dewpoint_temperature","VIS_station_visibility","PTDY_pressure_tendency","TIDE_water_level","station_name"]

combined_files = []
for url in source_urls:
    #retrieve station name from url
    pattern = '2/(.*?)\.'
    station_name = re.search(pattern, url).group(1)
    if station_name == 'KBQX': station_name = 'KAPT'
    #get data
    file = urllib.request.urlopen(url)
    current_file = []
    for line in file:
        decoded_line = line.decode("utf-8")
        if decoded_line.startswith('#'): #skip header
            continue
        dl_station = decoded_line + station_name #added station name as column
        current_file.append(dl_station.split()) #split data by blankspace
    combined_files.append(current_file) 
    #clean up header
    #del file_as_is[:2] #removed first two rows (headers)
#combined_files.insert(0,header) #adding in clean header
#     #save as csv
file_with_header = flatten(combined_files)
file_with_header.insert(0,header) #adding in clean header
np.savetxt("all_stations.csv",file_with_header,delimiter=",",fmt='% s')

