import streamlit as st

# Initialize the login state if not already set
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Function to display the login page
def login_page():
    st.title("Login Page")
    st.write("Please enter your credentials to continue.")

    # Email and password input fields
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    # Login button
    if st.button("Login"):
        # Simple username and password check
        if email and password:
            st.session_state.logged_in = True
            st.success("Login successful!")
        else:
            st.error("Incorrect username or password.")

# Function to display the dashboard page after login
def dashboard_page():
    st.title("Main Dashboard")
    st.write("Welcome to the main dashboard! You are now logged in.")

    # Example actions on the dashboard
    st.subheader("Available Actions:")
    st.button("Do Something")
    st.button("Run Report")
    st.button("Show Data")

    # Logout button
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.experimental_rerun()  # Force page refresh to go back to login

# Show login page if not logged in
if not st.session_state.logged_in:
    login_page()
else:
    dashboard_page()
