import streamlit as st
import folium
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim

st.set_page_config(page_title="sUMAKcess", layout="wide")

# ---------------- HOME PAGE ----------------
st.title("🐦sUMAKcess")

menu = st.radio(
    "Navigation",
    ["Home", "Accessibility Explorer", "Submit Report", "Healthcare", "Emergency SOS"],
    horizontal=True
)

# ---------------- HOME ----------------
if menu == "Home":
    st.subheader("How can we help today?")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🚨 EMERGENCY SOS", use_container_width=True):
            st.warning("Emergency Alert Sent (Demo Mode)")

    with col2:
        if st.button("🔎 Find Accessible Places", use_container_width=True):
            st.session_state.page = "Accessibility Explorer"

    st.divider()

    st.write("Quick Actions:")
    st.button("📝 Submit Accessibility Report")
    st.button("🏥 Accessible Healthcare")

# ---------------- MAP ----------------
elif menu == "Accessibility Explorer":
    st.subheader("Accessibility Map")

    m = folium.Map(location=[14.312, 121.111], zoom_start=14)

    folium.Marker(
        [14.312, 121.111],
        popup="Accessible Ramp - Santa Rosa"
    ).add_to(m)

    st_folium(m, width=900, height=500)

# ---------------- REPORT ----------------
elif menu == "Submit Report":
    st.subheader("Submit Accessibility Report")

    location_option = st.radio(
        "Choose Location Method",
        ["Use My Current Location", "Search Location"]
    )

    if location_option == "Search Location":
        address = st.text_input("Enter Address")
        if address:
            geolocator = Nominatim(user_agent="sumakcess")
            location = geolocator.geocode(address)
            if location:
                st.success(f"Latitude: {location.latitude}")
                st.success(f"Longitude: {location.longitude}")

    issue = st.text_area("Describe the accessibility issue")

    if st.button("Submit Report"):
        st.success("Report Submitted (Demo Mode)")

# ---------------- HEALTHCARE ----------------
elif menu == "Healthcare":
    st.subheader("Accessible Healthcare Services")

    st.write("🏥 Santa Rosa Community Hospital")
    st.write("♿ Wheelchair accessible entrance")

# ---------------- SOS ----------------
elif menu == "Emergency SOS":
    st.subheader("Emergency SOS")

    if st.button("SEND SOS ALERT"):
        st.error("SOS Alert Triggered (Demo Mode)")



