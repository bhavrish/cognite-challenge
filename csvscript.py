import csv
import json
from urllib.request import HTTPDefaultErrorHandler
import pandas as pd
import sys, getopt, pprint, os
from dotenv import load_dotenv
from pymongo import MongoClient
#CSV to JSON Conversion
csvfile = open('all_stations.csv', 'r')
reader = csv.DictReader( csvfile )
load_dotenv()   
password = os.environ.get('password')
passw = "mongodb+srv://coghack:" + password + "@cognitedash.uadlm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
cluster = MongoClient(passw)

d = cluster.samples
db = d["data3"]
# db.segment.drop()

header = ["year", "month", "day", "hour", "minute", "WDIR_wind_direction","WSPD_wind_speed","GST_gust_speed","WVHT_wave_height","DPD_dominant_wave_period","APD_average_wave_period","MWD_wave_degree","PRES_sea_level_pressure","ATMP_air_temperature","WTMP_sea_surface_temperature","DEWP_dewpoint_temperature","VIS_station_visibility","PTDY_pressure_tendency","TIDE_water_level","station_name"]
headernew = ["year", "month", "day", "hour", "minute", "WDIR_wind_direction","WSPD_wind_speed","station_name"]
count = 0
for each in reader:
    row = {}
    row["_id"] = count
    for field in header:
        if field in headernew:
            print(field)
            row[field]=each[field]
    
    print(row)
    db.insert_one(row)
    count += 1