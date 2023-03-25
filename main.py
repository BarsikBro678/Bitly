import argparse
import logging
import os
from urllib.parse import urlparse

from dotenv import load_dotenv
import reqests


def shorten_link(token, url):
    url = "https://api-ssl.bitly.com/v4/bitlinks"
    headers = {
        "Authorization": "Bearer {}".format(token),
    }
    payload = {
        "long_url": url,
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()["link"]


def count_clicks(token, url):
    url_parts = urlparse(url)
    user_url = "{netloc}{path}".format(netloc=url_parts.netloc, path=url_parts.path)
    url = "https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary".format(user_url)
    headers = {
        "Authorization": "Bearer {}".format(token),
    }
    payload = {
        "units": "-1",
    }
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    return response.json()["total_clicks"]


def is_bitlink(token, url):
    url_parts = urlparse(url)
    short_url = "{netloc}{path}".format(netloc=url_parts.netloc, path=url_parts.path)
    url = "https://api-ssl.bitly.com/v4/bitlinks/{}".format(short_url)
    headers = {
        "Authorization": "Bearer {}".format(token),
    }
    response = requests.get(url, headers=headers)
    return response.ok


def main():
    load_dotenv()
    bitly_token = os.environ["BITLY_TOKEN"]
    parser = argparse.ArgumentParser(
        description='Описание что делает программа'
    )
    parser.add_argument("user_url", help="Введите ссылку: ")
    args = parser.parse_args()
    try:
        if is_bitlink(bitly_token, args.user_url):
            print(count_clicks(bitly_token, args.user_url))
        else:
            print("Битлинк: ", shorten_link(bitly_token, args.user_url))
    except requests.exceptions.HTTPError:
        logging.exception("Ошибка при запросе bitly")


if __name__ == "__main__":
    main()
