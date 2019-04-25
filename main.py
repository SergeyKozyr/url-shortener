import requests
import os
import argparse
from dotenv import load_dotenv


def shorten_url(long_url, header):
  url = 'https://api-ssl.bitly.com/v4/bitlinks'
  payload = {"long_url": long_url}
  response = requests.post(url, headers=header, json=payload)
  if response.ok:
    return response.json()['id']


def count_clicks(bitlink, header):
  url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
  payload = {'unit': 'day', 'units': -1}
  response = requests.get(url, headers=header, json=payload)
  if response.ok:
    return response.json()['total_clicks']


def main(header):
  parser = argparse.ArgumentParser()
  parser.add_argument('link')
  args = parser.parse_args()
  link = args.link
  url = f'https://api-ssl.bitly.com/v4/bitlinks/{link}'
  payload = {'bitlink': link}
  response = requests.get(url, headers=header, json=payload)
  if response.ok:
    click_count = count_clicks(link, header)
    if click_count is None:
      print('incorrect url')
    else:
      print(f'total clicks: {click_count}')
  else:
    short_url = shorten_url(link, header)
    if short_url is None:
      print('incorrect url')
    else:
      print(short_url)


if __name__ == "__main__":
  load_dotenv()
  token = os.getenv("TOKEN")
  auth_header = {'Authorization': f'Bearer {token}'}
  main(auth_header)
