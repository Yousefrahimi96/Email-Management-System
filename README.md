
# 📧 Streamlit Email Dashboard

A secure, browser-based email dashboard built with [Streamlit](https://streamlit.io/). Users can log in with their email and password, and send plain text emails with optional file attachments via Gmail SMTP. Only pre-approved users are allowed access.

---

## 🚀 Features

- 🔐 Email & password login (with validation)
- ✅ Whitelisted users only
- 📧 Compose and send plain-text emails
- 📎 Upload and send file attachments (e.g., `.txt`, `.pdf`, `.jpg`)
- 🔁 Session state management with logout functionality
- 📬 Uses Gmail SMTP for sending emails

---

## 📦 Requirements

- Python 3.8+
- `streamlit==1.45.0`

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ⚙️ How to Run

```bash
streamlit run main.py
```

---

## 🔑 Gmail Note

To use your Gmail account for sending emails, you must:

1. Enable 2-step verification in your Google Account.
2. Generate an [App Password](https://support.google.com/accounts/answer/185833?hl=en).
3. Use that app password instead of your normal Gmail password when logging in.

---

## 👥 Whitelisted Users

Only the email addresses listed in the `ALLOWED_USERS` list inside `main.py` are allowed to log in. You can modify this list as needed:

```python
ALLOWED_USERS = ["admin@example.com", "user1@gmail.com"]
```

---

## 📁 File Attachments

Users can attach a file to each email. Supported types include (but are not limited to): `.pdf`, `.txt`, `.png`, `.jpg`, `.zip`, etc.

---

## 🔐 Security Warning

- Do **not** store plain-text passwords in production.
- Use encrypted secrets or environment variables.
- Consider using OAuth 2.0 or secure token-based login for public use cases.

---
