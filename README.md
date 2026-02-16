# Secure Authentication Portal (Demo)

A small Flask demo app that shows a login flow with a mock MFA step and a styled dashboard.

## Features

- Login form with demo credentials
- MFA step with a one-time code printed in the terminal
- Simple dashboard after successful verification
- Cyber-themed UI styling

## Tech Stack

- Python
- Flask
- HTML/CSS

## Project Structure

- app.py - Flask app and routes
- templates/ - HTML templates
- static/ - CSS styles
- requirements.txt - Python dependencies

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```
pip install -r requirements.txt
```

## Run

```
python app.py
```

Open http://127.0.0.1:5000 in your browser.

## Demo Credentials

- Username: user
- Password: U$eR@12345

After logging in, check the terminal output for the demo MFA code and enter it on the MFA page.

## Notes

- This is a demo app with hard-coded credentials and a mock MFA flow.
- The MFA code is not sent anywhere; it is printed to the server console.
