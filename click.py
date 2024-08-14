import configparser
import random
import time
import requests

def load_config(file_path='config.ini'):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config

def get_random_choice(config, section, key):
    items = config.get(section, key).split(',')
    return random.choice(items).strip()

def send_get_request(url, user_agent):
    headers = {'User-Agent': user_agent}
    try:
        response = requests.get(url, headers=headers)
        print(f"Request to {url} with agent {user_agent} returned status {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request to {url} failed: {e}")

def main():
    config = load_config()

    base_time_interval = int(config['SETTINGS']['time_interval'])

    while True:
        url = get_random_choice(config, 'WEBSITES', 'urls')
        user_agent = get_random_choice(config, 'BROWSER_AGENTS', 'agents')

        send_get_request(url, user_agent)

        # Add randomness to the time interval
        random_seconds = random.randint(-30, 30)
        sleep_time = base_time_interval + random_seconds
        print(f"Sleeping for {sleep_time} seconds before next request")
        time.sleep(sleep_time)

if __name__ == "__main__":
    main()
