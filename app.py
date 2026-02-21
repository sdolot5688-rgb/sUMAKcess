import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd
import streamlit as st

st.set_page_config(page_title="sUMAKcess PH", layout="wide")

# Custom Modern UI Styling
st.markdown("""
<style>

html, body, [class*="css"]  {
    font-family: 'Segoe UI', sans-serif;
}

.main {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}

h1, h2, h3 {
    color: #00E5FF;
}

.stButton>button {
    background-color: #00E5FF;
    color: black;
    border-radius: 12px;
    padding: 0.6em 1.2em;
    font-weight: bold;
    border: none;
    transition: 0.3s;
}

.stButton>button:hover {
    background-color: #00B8D4;
    transform: scale(1.05);
}

.stTextInput>div>div>input,
.stNumberInput input,
.stSelectbox div {
    border-radius: 10px;
}

.section-card {
    background-color: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="sUMAKcess", layout="wide")

t.markdown("""
<h1 style='text-align: center; font-size: 50px;'>
🚀 sUMAKcess            
</h1>
<p style='text-align: center; font-size:18px; color:#ccc;'>
Accessibility & Safety Platform for Inclusive Communities
</p>
""", unsafe_allow_html=True)

# Sidebar Navigation
menu = st.sidebar.radio(
    "Navigation",
    ["Accessibility Map", "Report Issue", "Health Services", "SOS"]
)
menu = st.sidebar.selectbox(
    "Navigation",
    ["Accessibility Map", "Health Services Access", "Safety Alert & SOS", "Report Accessibility Problem"]
)
if menu == "Accessibility Map":
    st.header("🗺️ Accessibility Map")


# Dummy Data Storage
if "locations" not in st.session_state:
    st.session_state.locations = []

# ==============================
# Accessibility Map
# ==============================

if menu == "Accessibility Map":
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
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
    st.markdown('</div>', unsafe_allow_html=True)
# ==============================
# Health Services Access
# ==============================
elif menu == "Health Services Access":
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.header("Accessible Health Services")

    st.info("This section will display accessible clinics & hospitals.")

    st.write("Example:")
    st.write("- Manila Medical Center")
    st.write("- Philippine General Hospital")
    st.write("- Quezon City General Hospital")
    st.markdown('</div>', unsafe_allow_html=True)
# ==============================
# Safety Alert & SOS
# ==============================
elif menu == "Safety Alert & SOS":
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.header("Emergency Safety Alert")

    if st.button("🚨 SEND SOS ALERT"):
        st.error("Emergency Alert Sent with GPS Location (Simulated)")

    st.write("Shake Detection (Mobile version feature)")
    st.write("• Shake phone for 10 seconds")
    st.write("• Confirmation prompt appears")
    st.write("• Sends emergency notification")
    st.markdown('</div>', unsafe_allow_html=True)
# ==============================
# Report Accessibility Problem
# ==============================
elif menu == "Report Accessibility Problem":
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.header("Report Barrier or Issue")

    issue = st.text_area("Describe the issue")
    photo = st.file_uploader("Upload photo of barrier", type=["jpg", "png"])

    if st.button("Submit Report"):
        if issue:
            st.success("Report Submitted for Community Validation")

    st.markdown('</div>', unsafe_allow_html=True)

