from os import getenv
from dotenv import load_dotenv
load_dotenv()

API_ID = int(getenv("API_ID", "20366634"))
API_HASH = getenv("API_HASH", "72095ec36984aa9ceb0dbaa9cec31559")

BOT_TOKEN = getenv("BOT_TOKEN", "7781735913:AAFa3jydrpzBCyULjVZ6hoYdsdkwDOthd_o")
LOG_ID = int(getenv("LOG_ID", "-1002640844591"))

MONGO_DB_URI = getenv("MONGO_DB_URI", ")mongodb+srv://rohitreddyathuru:R6Co7MOjTYQOAqcq@cluster0.xrwjpl9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
SUDO_USER = list(map(int, getenv("SUDO_USER", "20366634").split()))
