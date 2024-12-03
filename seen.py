# Watermark: https://t.me/mizegerddev & https://github.com/mizegerd-tech

import requests
import threading
import sys

# Semaphore to limit the number of concurrent threads
# Decrease this value if you encounter problems with your CPU/RAM usage.
max = threading.Semaphore(value=500)
threads = []

# Read the list of proxies from the file
with open('proxy.txt', 'r') as list:
    proxies = list.readlines()

def fetchData(channel='google', post='1', proxy=None):
    """
    Fetch data from the specified Telegram channel post using the given proxy.
    
    Args:
        channel (str): The Telegram channel name.
        post (str): The post ID.
        proxy (str): The proxy to use for the request.
    
    Returns:
        dict: A dictionary containing the key and cookie if successful.
        bool: False if the request fails.
    """
    try:
        r = requests.get(f'https://t.me/{channel}/{post}?embed=1', timeout=20, proxies={'https': proxy})
        cookie = r.headers['set-cookie'].split(';')[0]
        key = r.text.split('data-view="')[1].split('"')[0]
        if 'stel_ssid' in cookie:
            return {'key': key, 'cookie': cookie}
        else:
            return False
    except Exception as e:
        return False

def addViewToPost(channel='google', post='1', key=None, cookie=None, proxy=None):
    """
    Add a view to the specified Telegram channel post using the given key, cookie, and proxy.
    
    Args:
        channel (str): The Telegram channel name.
        post (str): The post ID.
        key (str): The key obtained from fetchData.
        cookie (str): The cookie obtained from fetchData.
        proxy (str): The proxy to use for the request.
    
    Returns:
        str: The response text if successful.
        bool: False if the request fails.
    """
    try:
        r = requests.get(f'https://t.me/v/?views={key}', timeout=20, headers={
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
            'referer': f'https://t.me/{channel}/{post}?embed=1',
            'cookie': cookie
        }, proxies={'https': proxy})
        return r.text
    except Exception as e:
        return False

def run(channel, post, proxy):
    """
    Run the process of fetching data and adding a view to the post using the given proxy.
    
    Args:
        channel (str): The Telegram channel name.
        post (str): The post ID.
        proxy (str): The proxy to use for the request.
    """
    max.acquire()
    s = fetchData(channel, post, f'https://{proxy}')
    if isinstance(s, dict):
        l = addViewToPost(channel, post, s['key'], s['cookie'], f'https://{proxy}')
        if l != False:
            print(f'Proxy {proxy} finished its job successfully!')
    max.release()
    print(f'Thread with proxy {proxy} has been terminated.')

# Start a new thread for each proxy
for proxy in proxies:
    p = proxy.strip()
    thread = threading.Thread(target=run, args=(sys.argv[1], sys.argv[2], p))
    threads.append(thread)
    thread.start()
    print(f'Started new thread with proxy {p}')