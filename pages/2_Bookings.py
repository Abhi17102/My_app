import streamlit as st

st.set_page_config(page_title="Booking")

# Check if user and concert data are present
if not st.session_state.get("logged_in", False):
    st.warning("Please login first.")
    st.switch_page("app.py")

if "selected_concert" not in st.session_state:
    st.warning("Please select a concert to book.")
    st.switch_page("pages/1_Concerts.py")

concert = st.session_state.selected_concert

st.title("Booking Details")
st.subheader(f"You are booking: {concert['name']}")
st.text(f"Date: {concert['date']}")
st.text(f"Location: {concert['location']}")

# Booking form
name = st.text_input("Your Name")
tickets = st.number_input("Number of Tickets", min_value=1, max_value=10, step=1)

if st.button("Confirm Booking"):
    if name:
        st.success(f"Thank you {name}! You have booked {tickets} tickets for {concert['name']}.")
        # You can also store this info in session_state or a database
    else:
        st.error("Please enter your name.")

if st.button("Back to Concerts"):
    st.switch_page("pages/1_Concerts.py")
