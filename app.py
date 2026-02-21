import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

st.set_page_config(page_title="sUMAKcess PH", layout="wide")

st.title("sUMAKcess PH")
st.subheader("Accessible. Safe. Inclusive.")

# Sidebar Navigation
menu = st.sidebar.selectbox(
    "Navigation",
    ["Accessibility Map", "Health Services Access", "Safety Alert & SOS", "Report Accessibility Problem"]
)

# Dummy Data Storage
if "locations" not in st.session_state:
    st.session_state.locations = []

# ==============================
# Accessibility Map
# ==============================
if menu == "Accessibility Map":
    st.header("Accessibility Mapping System")

    location_name = st.text_input("Location Name")
    lat = st.text_input("Latitude")
    lon = st.text_input("Longitude")
    access_type = st.selectbox("Accessibility Type", ["Accessible", "Not Accessible"])

    if st.button("Add Report"):
        if location_name and lat and lon:
            st.session_state.locations.append(
                {"name": location_name, "lat": float(lat), "lon": float(lon), "type": access_type}
            )
            st.success("Location Added Successfully")

    # Generate Map
    m = folium.Map(location=[14.5995, 120.9842], zoom_start=12)

    for loc in st.session_state.locations:
        color = "green" if loc["type"] == "Accessible" else "red"
        folium.Marker(
            [loc["lat"], loc["lon"]],
            popup=loc["name"],
            icon=folium.Icon(color=color)
        ).add_to(m)

    st_folium(m, width=1000, height=500)

# ==============================
# Health Services Access
# ==============================
elif menu == "Health Services Access":
    st.header("Accessible Health Services")

    st.info("This section will display accessible clinics & hospitals.")

    st.write("Example:")
    st.write("- Manila Medical Center")
    st.write("- Philippine General Hospital")
    st.write("- Quezon City General Hospital")

# ==============================
# Safety Alert & SOS
# ==============================
elif menu == "Safety Alert & SOS":
    st.header("Emergency Safety Alert")

    if st.button("🚨 SEND SOS ALERT"):
        st.error("Emergency Alert Sent with GPS Location (Simulated)")

    st.write("Shake Detection (Mobile version feature)")
    st.write("• Shake phone for 10 seconds")
    st.write("• Confirmation prompt appears")
    st.write("• Sends emergency notification")

# ==============================
# Report Accessibility Problem
# ==============================
elif menu == "Report Accessibility Problem":
    st.header("Report Barrier or Issue")

    issue = st.text_area("Describe the issue")
    photo = st.file_uploader("Upload photo of barrier", type=["jpg", "png"])

    if st.button("Submit Report"):
        if issue:
            st.success("Report Submitted for Community Validation")