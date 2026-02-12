"""Everything such as APIs and tokens for the bot, commands and functions to run on"""

from os import getenv, environ
from dotenv import load_dotenv
from sqlite3 import connect

load_dotenv()
TOKEN = getenv("token")
WEATHER = getenv("weather_api")
TOPGG = getenv("topgg")
TOPGG_AUTH = getenv("topgg_auth")
DB_AUTH = getenv("db_auth")
WEBHOOK = getenv("report_webhook")
BB_WEBHOOK = getenv("botban_webhook")
TENOR = getenv("tenor")
CLIENTKEY = getenv("client_key")
JEANNE = getenv("jeanne_album")
SABER = getenv("saber_album")
WALLPAPER = getenv("wallpaper_album")
MEDUSA = getenv("medusa_album")
ANIMEME = getenv("animeme_album")
NEKO = getenv("neko_album")
MORGAN = getenv("morgan_album")
KITSUNE = getenv("kitsune_album")
CATBOX_HASH = str(getenv("catbox_hash"))
BADGES = getenv("badges_album")
STATUS_WEBHOOK = getenv("status")

GELBOORU_API = getenv("GELBOORU_API_KEY")
GELBOORU_USER = getenv("GELBOORU_USER_ID")
RULE34_API = getenv("RULE34_API_KEY")
RULE34_USER = getenv("RULE34_USER_ID")
OPENAI_API = getenv("OPENAI_API_KEY")

db = connect("database.db", autocommit=True)

# Migrated to the Klipy API
# hug = f"https://tenor.googleapis.com/v2/search?q=hug%20anime&key={TENOR}&client_key={CLIENTKEY}&limit=50"
hug = f"https://api.klipy.com/v2/search?q=hug%20anime&key={TENOR}&client_key={CLIENTKEY}&limit=50"
slap = f"https://api.klipy.com/v2/search?q=slap%20anime&key={TENOR}&client_key={CLIENTKEY}&limit=50"
smug = f"https://api.klipy.com/v2/search?q=smug%20anime&key={TENOR}&client_key={CLIENTKEY}&limit=50"
poke = f"https://api.klipy.com/v2/search?q=poke%20anime&key={TENOR}&client_key={CLIENTKEY}&limit=50"
pat = f"https://api.klipy.com/v2/search?q=headpat%20anime&key={TENOR}&client_key={CLIENTKEY}&limit=50"
kiss = f"https://api.klipy.com/v2/search?q=kiss%20anime&key={TENOR}&client_key={CLIENTKEY}&limit=50"
tickle = f"https://api.klipy.com/v2/search?q=tickle%20anime&key={TENOR}&client_key={CLIENTKEY}&limit=50"
baka = f"https://api.klipy.com/v2/search?q=baka%20anime&key={TENOR}&client_key={CLIENTKEY}&limit=50"
feed = f"https://api.klipy.com/v2/search?q=feed%20anime&key={TENOR}&client_key={CLIENTKEY}&limit=50"
cry = f"https://api.klipy.com/v2/search?q=cry%20anime&key={TENOR}&client_key={CLIENTKEY}&limit=50"
bite = f"https://api.klipy.com/v2/search?q=bite%20anime&key={TENOR}&client_key={CLIENTKEY}&limit=50"
blush = f"https://api.klipy.com/v2/search?q=blush%20anime&key={TENOR}&client_key={CLIENTKEY}&limit=50"
cuddle = f"https://api.klipy.com/v2/search?q=cuddle%20anime&key={TENOR}&client_key={CLIENTKEY}&limit=50"
dance = f"https://api.klipy.com/v2/search?q=dance%20anime&key={TENOR}&client_key={CLIENTKEY}&limit=50"
