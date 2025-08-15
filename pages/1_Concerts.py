import streamlit as st

st.set_page_config(page_title="Concerts")

# Make sure user is logged in
if not st.session_state.get("logged_in", False):
    st.warning("Please login first.")
    st.switch_page("app.py")

st.title("Available Concerts")

concerts = [
    {"id": 1, "name": "Rock Nation", "date": "July 15, 2025", "location": "Mumbai"},
    {"id": 2, "name": "Jazz Nights", "date": "August 5, 2025", "location": "Delhi"},
    {"id": 3, "name": "EDM Blast", "date": "September 10, 2025", "location": "Goa"},
]

# Display each concert
for concert in concerts:
    with st.container():
        st.subheader(concert["name"])
        st.text(f"Date: {concert['date']}")
        st.text(f"Location: {concert['location']}")
        book_button = st.button(f"Book {concert['name']}", key=concert["id"])
        if book_button:
            # Store selected concert in session
            st.session_state.selected_concert = concert
            st.switch_page("pages/2_Bookings.py")

if st.button("Logout"):
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.switch_page("app.py")
