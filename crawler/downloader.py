import requests
import time
import random

class Downloader:
    def __init__(self, proxies=None, user_agents=None):
        self.session = requests.Session()
        self.proxies = proxies or []
        self.user_agents = user_agents or [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        ]

    def fetch(self, url):
        headers = {"User-Agent": random.choice(self.user_agents)}
        proxy = {"http": random.choice(self.proxies)} if self.proxies else None
        resp = self.session.get(url, headers=headers, proxies=proxy, timeout=10)
        resp.raise_for_status()
        time.sleep(random.uniform(1, 3))  # polite delay
        return resp.text
