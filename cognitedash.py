import streamlit as st
import pandas as pd
import pymongo
from pymongo import MongoClient
import os
from dotenv import load_dotenv
import pandas as pd
from pprint import pprint

load_dotenv()   

st.set_page_config(layout="wide")

password = os.environ.get('password')
passw = "mongodb+srv://coghack:" + password + "@cognitedash.uadlm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
cluster = MongoClient(passw)

db = cluster.samples
collection = db["data3"]


# data = pd.DataFrame(list(collection.find({ "location": "KIKT"})))
# pprint(data.head())


# temp = db.collection.find()
# # data = pd.DataFrame(list(temp))
#print(data.list_database_names())






row1_1, row1_2 = st.columns((2,3))

with row1_1:
    st.title("Cognite Wind Forecasting")
    stat_sel = st.selectbox('Select a station', ['KIKT','KAPT','KMIS'])
    date_sel = st.date_input('Select a date from 12/21/2021 to 1/29/2022') 
    year = str(date_sel.year)
    mon = date_sel.month
    if mon == 1 or mon == 2 or mon == 3 or mon == 4 or mon == 5 or mon == 6 or mon == 7 or mon == 8 or mon == 9:
        month = '0' + str(mon)
    else:
        month = str(mon)
    da = date_sel.day
    if da == 1 or da == 2 or da == 3 or da == 4 or da == 5 or da == 6 or da == 7 or da == 8 or da == 9:
        day = '0' + str(da)
    else:
        day = str(da)
    print(year, month, day)

# #add day month year here
# # data = pd.DataFrame(list(collection.find({ "year": year, "month" : month, "day" : day, "station_name": stat_sel})))
data = pd.DataFrame(list(collection.find({"year": year, "month" : month, "station_name": stat_sel})))

print(data)

with row1_2:
    st.write(
    """
    ##
    Welcome to our live wind forecasting dashboard, brought to you by Cognite and Fondren 425!
    Choose a station and a date from the last 45 days to display a time series plot of wind speed and direction, as
    well as a polar plot of averages. Underneath, you'll find a plot of predicted wind speed and direction
    trends 72 hours out from today. 
    """)


row2_1, row2_2 = st.columns((2,1))

with row2_1:
    st.write("**Wind speed and direction at station %s on %s**" % (stat_sel, date_sel))

    #map(data, midpoint[0], midpoint[1], 11)

with row2_2:
    st.write("**Polar plot of averages**")
    #map(data, la_guardia[0],la_guardia[1], zoom_level)


st.write("")
st.write("")
st.write("")
st.write("**Forecasted wind speed and direction 72 hours from today**")

row4_1, row4_2 = st.columns((2,1))
with row4_2:
    st.image('cogniteimage.png')


