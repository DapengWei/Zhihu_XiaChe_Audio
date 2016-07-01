#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import os
import requests
import zhihu_spider
import baidu_sound
import time
import subprocess

global zhihudaily_api
zhihudaily_api = "http://zhihudaily.ahorn.me/api/1"

global baidu_token_url
baidu_token_url = "https://openapi.baidu.com/oauth/2.0/token"

global baidu_api_url
baidu_api_url = "http://tsn.baidu.com/text2audio"

global baidu_API_Key
baidu_API_Key = ""

global baidu_Secret_Key
baidu_Secret_Key = ""


def main():
    zhihu_list = zhihu_spider.get_today_list(zhihudaily_api)
    sound_string = []
    for zhihu_item in zhihu_list:
        if re.search(u'\u778e\u626f', zhihu_item[u"Title"] ) is not None:
            zhihu_xiache_id = zhihu_item[u"Id"]
            break

    zhihu_contents = zhihu_spider.get_content(zhihu_xiache_id)
    for zhihu_title in zhihu_contents:
        sound_string.append(zhihu_title)
        for answer in zhihu_contents[zhihu_title]:
            answer_string = answer[0]
            for answer_detail in answer[-1]:
                answer_string = answer_string + ";" + answer_detail
            sound_string.append(answer_string)

    tmp_num = 0
    mp3_files = []
    for sound_data in sound_string:
        file_id = ("temp%02d.mp3") % (tmp_num,)
        baidu_sound.baidu_string_sound(baidu_api_url, baidu_token_url, baidu_API_Key, baidu_Secret_Key, sound_data, file_id)
        tmp_num = tmp_num + 1
        mp3_files.append(file_id)

    current_dir = os.path.dirname(os.path.realpath(__file__))
    for mp3_file in mp3_files:
        subprocess.call("mplayer "+mp3_file, shell=True, cwd=current_dir)
        subprocess.call("rm -rf "+mp3_file, shell=True, cwd=current_dir)
        time.sleep(1)





if __name__ == "__main__":
    main()
