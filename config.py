import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "12557431"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "dbf930927f239982765d29cf6cb9a579")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://jaypck:ey8ZyUVRcKiiiO3A@cluster0.q7zla97.mongodb.net/?retryWrites=true&w=majority")
