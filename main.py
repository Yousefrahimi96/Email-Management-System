import streamlit as st
import smtplib
from email.mime.text import MIMEText

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
            # Store credentials in session state for email sending
            st.session_state.email = email
            st.session_state.password = password
            st.session_state.logged_in = True
            st.success("Login successful!")
            st.rerun()  # Refresh page to show dashboard
        else:
            st.error("Please enter both email and password.")

# Function to display the dashboard page after login
def dashboard_page():
    st.title("Main Dashboard")
    st.write("Welcome to the main dashboard! You are now logged in.")
    
    # Email form
    st.subheader("Send Email")
    subject = st.text_input("Subject:")
    to = st.text_input("To:")
    text = st.text_area("Email text:")
    
    # Send email button
    if st.button("Send Email"):
        if subject and to and text:
            # SMTP server settings
            smtp_server = "smtp.gmail.com"
            port = 587  # For starttls
            
            # Create message
            msg = MIMEText(text)
            msg['Subject'] = subject
            msg['From'] = st.session_state.email
            msg['To'] = to
            
            try:
                # Connect to server and send email
                server = smtplib.SMTP(smtp_server, port)
                server.starttls()  # Secure the connection
                server.login(st.session_state.email, st.session_state.password)
                server.send_message(msg)
                server.quit()
                st.success("Email sent successfully!")
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.error("Please fill in all fields.")
    
    # Logout button
    if st.button("Logout"):
        # Clear session state
        st.session_state.logged_in = False
        if 'email' in st.session_state:
            del st.session_state.email
        if 'password' in st.session_state:
            del st.session_state.password
        st.rerun()  # Force page refresh to go back to login

# Show login page if not logged in
if not st.session_state.logged_in:
    login_page()
else:
    dashboard_page()