# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 12:09:31 2024

@author: Olwith
"""

import streamlit as st
from pyproj import Proj, transform

# Function to convert UTM to WGS84
def utm_to_wgs84(easting, northing, zone_number, zone_letter):
    utm = Proj(proj='utm', zone=zone_number, ellps='WGS84', datum='WGS84', south=(zone_letter.lower() >= 'n'))
    wgs84 = Proj(proj='latlong', datum='WGS84')
    lon, lat = transform(utm, wgs84, easting, northing)
    return lon, lat
#Function to convert wgs84 to UTM
def wgs84_to_utm(lon,lat):
    wgs84 = Proj(proj='latlong', datum='WGS84')
    utm = Proj(proj='utm', zone=zone_number, ellps='WGS84', datum='WGS84', south=(zone_letter.lower() >= 'n'))
    easting, northing = transform(wgs84, utm, lon, lat)
    return easting, northing

# Function to convert WGS84 to Cassini
def wgs84_to_cassini(lon, lat):
    wgs84 = Proj(proj='latlong', datum='WGS84')
    cassini = Proj(proj='cass', lon_0=lon, lat_0=lat)
    easting, northing = transform(wgs84, cassini, lon, lat)
    return easting, northing

# Function to convert Cassini to WGS84
def cassini_to_wgs84(easting, northing, lon, lat):
    cassini = Proj(proj='cass', lon_0=lon, lat_0=lat)
    wgs84 = Proj(proj='latlong', datum='WGS84')
    lon, lat = transform(cassini, wgs84, easting, northing)
    return lon, lat

# Streamlit UI
st.title('Coordinate Conversion Calculator')

conversion_type = st.selectbox('Select Conversion Type', ['UTM to WGS84', 'WGS84 to Cassini', 'Cassini to WGS84'])

if conversion_type == 'UTM to WGS84':
    easting = st.number_input('Enter Easting:', value=0.0)
    northing = st.number_input('Enter Northing:', value=0.0)
    zone_number = st.number_input('Enter Zone Number:', value=32)
    zone_letter = st.text_input('Enter Zone Letter:', value='U')
    if st.button('Convert'):
        lon, lat = utm_to_wgs84(easting, northing, zone_number, zone_letter)
        st.write(f'Longitude: {lon}, Latitude: {lat}')

elif conversion_type == 'WGS84 to UTM':
    lon = st.number_input('Enter Longitude:', value=0.0)
    lat = st.number_input('Enter Latitude:', value=0.0)
    if st.button('Convert'):
        easting, northing = wgs84_to_utm(lon, lat)
        st.write(f'Easting: {easting}, Northing: {northing}')

elif conversion_type == 'WGS84 to Cassini':
    lon = st.number_input('Enter Longitude:', value=0.0)
    lat = st.number_input('Enter Latitude:', value=0.0)
    if st.button('Convert'):
        easting, northing = wgs84_to_cassini(lon, lat)
        st.write(f'Easting: {easting}, Northing: {northing}')

else:
    easting = st.number_input('Enter Easting:', value=0.0)
    northing = st.number_input('Enter Northing:', value=0.0)
    lon = st.number_input('Enter Central Meridian Longitude:', value=0.0)
    lat = st.number_input('Enter Central Meridian Latitude:', value=0.0)
    if st.button('Convert'):
        lon, lat = cassini_to_wgs84(easting, northing, lon, lat)
        st.write(f'Longitude: {lon}, Latitude: {lat}')
