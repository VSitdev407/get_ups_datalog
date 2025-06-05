import os

UPS_LIST = [
    {"name": "UPS_9F",  "url": "http://172.21.3.11/cgi-bin/dnpower.cgi?page=42&"},
    {"name": "UPS_8F",  "url": "http://172.21.4.10/cgi-bin/dnpower.cgi?page=42&"},
    {"name": "UPS_7F",  "url": "http://172.21.6.10/cgi-bin/dnpower.cgi?page=42&"},
    {"name": "UPS_3F",  "url": "http://172.21.5.14/cgi-bin/dnpower.cgi?page=42&"},
    {"name": "UPS_10F", "url": "http://172.21.2.13", "is_10f": True},
]

UPS_USERNAME = "admin"
UPS_PASSWORD = "misadmin"

# Set the target time for data extraction
TARGET_HOUR = 8
TARGET_MINUTE= 30
TIME_RANGE_MINUTES = 45

TEMP_CSV_FOLDER = os.path.join(os.getcwd(), 'temp_csv')

# Dropbox configuration Poweradmin
# Note: Replace these with your actual Dropbox credentials if you change a dropbox account.
# Make sure to keep these credentials secure and not expose them in public repositories.
DROPBOX_REFRESH_TOKEN = "BJcWaTN3aMEAAAAAAAAAAbJNwqLLZU0V7X1fXPyKJDNfTpxOfEz8aCxoS_hKPi-s"
DROPBOX_APP_KEY = "pmnzyptjnq8cqgr"
DROPBOX_APP_SECRET = "2gdwzbiq3cmh5yw"
DROPBOX_UPLOAD_PATH = "/ups_datalog/"

