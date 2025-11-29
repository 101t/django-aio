import os

DEFAULT_RETRY_DELAY = int(os.environ.get('DEFAULT_RETRY_DELAY', default=5))  # 15 seconds
MAX_RETRIES = int(os.environ.get('MAX_RETRIES', default=5))
