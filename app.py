import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="sUMAKcess", layout="wide")

# ------------------ SIDEBAR MENU ------------------
st.sidebar.title("☰ sUMAKcess Menu")
page = st.sidebar.radio(
    "Navigate",
    ["Home", "Emergency SOS", "Healthcare", "About"]
)

# ------------------ HOME (WAZE STYLE) ------------------
if page == "Home":

    st.title("♿ sUMAKcess")

    # Search Bar (Main Feature)
    search = st.text_input("🔎 Find accessible place...")

    st.divider()

    # Map
    st.subheader("Accessibility Map")

    m = folium.Map(location=[14.312, 121.111], zoom_start=14)

    # Example marker
    folium.Marker(
        [14.312, 121.111],
        popup="♿ Accessible Ramp - Santa Rosa",
        tooltip="Accessible Ramp"
    ).add_to(m)

    map_data = st_folium(m, width=1200, height=500)

    st.divider()

    # Floating-like Action Section
    st.subheader("Quick Actions")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("➕ Submit Report", use_container_width=True):
            st.session_state.page = "report"

    with col2:
        if st.button("🚨 Emergency SOS", use_container_width=True):
            st.session_state.page = "Emergency SOS"

    with col3:
        if st.button("🏥 Healthcare", use_container_width=True):
            st.session_state.page = "Healthcare"

# ------------------ SOS ------------------
elif page == "Emergency SOS":

    st.title("🚨 Emergency SOS")

    st.warning("Use only during real emergencies.")

    if st.button("SEND SOS ALERT", use_container_width=True):
        st.error("SOS Alert Sent (Demo Mode)")

# ------------------ HEALTHCARE ------------------
elif page == "Healthcare":

    st.title("🏥 Accessible Healthcare")

    st.success("Nearby Accessible Hospitals")

    st.write("• Santa Rosa Community Hospital")
    st.write("• Medical City South Luzon")
    st.write("• Accessible Pharmacy")

# ------------------ ABOUT ------------------
elif page == "About":

    st.title("About sUMAKcess")

    st.write("""
    sUMAKcess is a smart accessibility navigation platform
    designed to help persons with disabilities and seniors
    find accessible locations and stay safe.
    """)
