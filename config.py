from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "BAGveF8AEEMFwvFdVSPxF7fe9XBl0XGH07yQrua0L4jy-l8Yl44dRIV-FRk_v9Yvfye9nR_P2kFCug9B_3d5ybv8iggDRU68YZxipbdrU4OmaKza10WncRZL7GmOje-362xceTXQaZE9k8nWlQ4UhevUG9WV96pb2ohnB88khVgAvuc_qqVYb9j2Pkd_S8cn5XvKy2n8cC1WyTM1aBThocumnIIV6O2vYbLNs3j7DRLAPC2I6FsgCDcnEKovMZ8OaoLm3d_RKfr88sknLCy0GA3XG-SC-TzzOInRNNFyL9U9d_9MamyDOtw2y0zmbU85qRtYqlnpRYyICRfiJrLdWotqDSc-VwAAAAGzTENpAA")
API_ID = int(getenv("API_ID", "28276831"))
API_HASH = getenv("API_HASH", "e1d302d72df431cd419bb2267e2200b8")
BOT_TOKEN = getenv("BOT_TOKEN", "6869756562:AAFVzgPQEhop6aUg32XpWYWiOoYMZ07JYeI")
BOT_NAME = getenv("BOT_NAME", "Tekor Music") 
BOT_USERNAME = getenv("BOT_USERNAME", "@TekorMusicBot")
BOT_CHANNEL = getenv("BOT_CHANNEL", "-2230110337")
ASS_USERNAME = getenv("ASS_USERNAME", "@iremalls")
OWNER = getenv("OWNER", "6737592159")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", 500))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7303086953").split()))
