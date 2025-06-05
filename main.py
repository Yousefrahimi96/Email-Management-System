import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import re

# List of allowed users (you can load this from a database or file)
ALLOWED_USERS = ["admin@example.com", "user1@gmail.com", "your_email@gmail.com"]

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Validate email format
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# Login page
def login_page():
    st.title("Login Page")
    st.write("Please enter your credentials to continue.")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if not email or not password:
            st.error("Please enter both email and password.")
        elif not is_valid_email(email):
            st.error("Invalid email format.")
        elif email not in ALLOWED_USERS:
            st.error("This email is not authorized to access the dashboard.")
        else:
            st.session_state.email = email
            st.session_state.password = password
            st.session_state.logged_in = True
            st.success("Login successful!")
            st.rerun()


def dashboard_page():
    st.title("Main Dashboard")
    st.write("Welcome to the dashboard.")

    st.subheader("Send Email")
    subject = st.text_input("Subject")
    to = st.text_input("To")
    text = st.text_area("Email Body")
    uploaded_file = st.file_uploader("Attach a file (optional)", type=None)

    if st.button("Send Email"):
        if not subject or not to or not text:
            st.error("Please fill in all fields.")
        elif not is_valid_email(to):
            st.error("Recipient email is invalid.")
        else:
            try:

                smtp_server = "smtp.gmail.com"
                port = 587
                sender_email = st.session_state.email
                sender_password = st.session_state.password

                message = MIMEMultipart()
                message["Subject"] = subject
                message["From"] = sender_email
                message["To"] = to

                message.attach(MIMEText(text, "plain"))

                # Attach file if provided
                if uploaded_file is not None:
                    file_data = uploaded_file.read()
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(file_data)
                    encoders.encode_base64(part)
                    part.add_header(
                        "Content-Disposition",
                        f"attachment; filename={uploaded_file.name}",
                    )
                    message.attach(part)


                server = smtplib.SMTP(smtp_server, port)
                server.starttls()
                server.login(sender_email, sender_password)
                server.send_message(message)
                server.quit()
                st.success("Email sent successfully!")

            except Exception as e:
                st.error(f"An error occurred: {e}")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.pop("email", None)
        st.session_state.pop("password", None)
        st.rerun()


if not st.session_state.logged_in:
    login_page()
else:
    dashboard_page()
