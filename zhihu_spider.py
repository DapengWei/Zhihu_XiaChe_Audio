#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import requests
from lxml import html

global header_info
header_info = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0'
    }


def get_today_list(page_url):
    daily_content = {}
    r = requests.get(page_url, headers=header_info, timeout=10)
    r.encoding = "utf-8"
    r_utf8 = unicode(r.content, "utf-8")
    daily_content_list = r.json()[0][u'Useddata']
    for daily_content in daily_content_list:
        local_time = time.strftime("%Y.%m.%d",time.localtime())
        if daily_content[u'Date'].split(" ")[0] == local_time:
            return daily_content[u"MainPages"]


def get_content(content_id):
    content_url = "http://daily.zhihu.com/story/" + str(content_id)
    answer_content = {}
    r = requests.get(content_url, headers=header_info, timeout=10)
    r.encoding = "utf-8"
    r_utf8 = unicode(r.content, "utf-8")
    root = html.document_fromstring(r_utf8)
    content_list_html = root.xpath("/html/body/div[@class='main-wrap content-wrap']")[0]
    content_title = content_list_html.xpath("div[@class='headline']/div[@class='img-wrap']/h1")[0].text
    answer_content[content_title] = []
    question_list = content_list_html.xpath("div[@class='content-inner']/div[@class='question']")
    for question_content in question_list:
        question_return_list = []
        question_title = question_content.xpath("h2[@class='question-title']")[0].text
        question_return_list.append(question_title)
        question_answer_list = question_content.xpath("div[@class='answer']")
        answer_return_list = []
        for question_answer_content in question_answer_list:
            question_answer_text = ""
            for line_answer in question_answer_content.xpath("div[@class='content']/p"):
                if line_answer.text is not None:
                    question_answer_text = question_answer_text + line_answer.text
            answer_return_list.append(question_answer_text)
        question_return_list.append(answer_return_list)
        answer_content[content_title].append(question_return_list)
    return answer_content


def main():
    test_list = get_list("http://zhihudaily.ahorn.me/api/1")
    for i in test_list:
        print i

if __name__ == "__main__":
    main()
