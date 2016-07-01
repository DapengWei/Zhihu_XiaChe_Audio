#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests


def get_baidu_token(token_url, API_Key, Secret_Key):
    token_post_data = {"grant_type": "client_credentials", "client_id": API_Key, "client_secret": Secret_Key}
    r = requests.post(token_url, data=token_post_data, timeout=10)
    r_json = r.json()[u'access_token']
    return r_json


def baidu_string_sound(api_url, token_url, API_Key, Secret_Key, input_string, file_name):
    baidu_token = get_baidu_token(token_url, API_Key, Secret_Key)
    cuid = "e68c0ec463a"
    sound_post_data = {"tex": input_string, "lan": "zh", "tok": baidu_token, "ctp": 1, "cuid": cuid, "spd": 5, "pit": 5, "vol": 5, "per": 0}
    r = requests.post(api_url, data=sound_post_data, stream=True, timeout=10)
    with open(file_name, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=512):
            fd.write(chunk)
    return True


def main():
    pass

if __name__ == "__main__":
    main()
