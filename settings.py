import os
import dotenv

dotenv.load_dotenv('.env')

HISTORY_JSON_PATH = os.environ.get('HISTORY_JSON_PATH', './history.json')
DISCORD_WEBHOOK_URL = os.environ.get('DISCORD_WEBHOOK_URL')
WATCH_INTERVAL_MINUTES = int(os.environ.get('WATCH_INTERVAL_MINUTES', '30'))

if DISCORD_WEBHOOK_URL is None:
    raise RuntimeError('DISCORD_WEBHOOK_URL is not set')
