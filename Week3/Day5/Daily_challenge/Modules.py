import requests
import time

url1 = 'https://google.com'
url2 = 'https://yahoo.com'
url3 = 'https://github.com'
url4 = 'https://python.org'
url5 = 'https://pypi.org'
url_list = [url1, url2, url3, url4, url5]
red = '\033[91m'
reset = '\033[0m'
green = '\033[92m'
blue = '\033[94m'
color = red

def get_time():
    for url in url_list:
        start_time = time.time()
        r = requests.get(url)
        status = r.status_code
        if status == 200:
            color = green    
        end_time = time.time()
        print(f"{url[8:]} took {end_time - start_time:.2f} seconds to load with status code {color}{status}{reset}")

get_time() 