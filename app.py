import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import plotly.express as px
from pathlib import Path

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='STHM',
    page_icon=':earth_americas:', # This is an emoji shortcode. Could be a URL too.
)

# -----------------------------------------------------------------------------
# Declare some useful functions.


# Placeholder for loading necessary data
# Replace with your actual data loading logic later
# reach_ids = pd.read_csv('reach_ids.csv')
try:
    # Make sure the file path is correct
    # df = pd.read_csv('data/nwis_sites1.csv', low_memory=False)
    # st.write(df)
except FileNotFoundError:
    st.error("File not found. Please check the file path.")
# nwis_sites = pd.read_csv('data/nwis_sites1.csv')
# nwid_flowlist = pd.read_csv('nwid_flowlist.csv')
# nwm_flow_fore = pd.read_csv('nwm_flow_fore.csv')

# Define UI
st.title("Hydrological Data Visualization")

# Date Range Input
st.sidebar.header("Select Date Range")
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2009-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("2009-12-31"))

# Map Component
st.header("Hydrological Map")
m = folium.Map(location=[38.5, -98.5], zoom_start=4)  # Adjust the initial location and zoom

# Add markers to the map (example, replace with your data)
# for index, row in nwis_sites.iterrows():
#     folium.Marker([row['lat'], row['lon']], popup=f"Site: {row['siteNumber']}").add_to(m)

# Render the map
st_data = st_folium(m, width=700, height=450)

# Interactive Plotly plot (replace with your actual plot data)
st.header("Flowline Plot")
if st_data["last_object_clicked"]:
    selected_site = st_data["last_object_clicked"]["id"]
    # selected_site_flow = nwid_flowlist[nwid_flowlist['siteNumber'] == int(selected_site)]
    # fig = px.line(selected_site_flow, x="Date", y="Flow")
    # st.plotly_chart(fig)
    st.write(f"Selected Site: {selected_site}")  # Replace with actual plot logic

# Performance Metrics (replace with your performance calculation logic)
st.header("Performance Metrics")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Calibration Performance (2009-2018)")
    # st.metric("Metric", "Value")  # Replace with your metrics
with col2:
    st.subheader("Performance During Selected Period")
    # st.metric("Metric", "Value")  # Replace with your metrics

# Additional plots
st.header("Forecast Plots")
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Forecast Plot")
    # st.plotly_chart(...)  # Replace with your plot logic
with col2:
    st.subheader("Reach Flow Plot")
    # st.plotly_chart(...)  # Replace with your plot logic
with col3:
    st.subheader("Test Plot")
    # st.plotly_chart(...)  # Replace with your plot logic

# Data Download
st.sidebar.header("Download Data")
st.sidebar.download_button("Download Data", "sample_data.csv")  # Replace with actual download logic
