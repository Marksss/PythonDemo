import requests_utils
from bs4 import BeautifulSoup
import re
from datetime import datetime


def get_hangzhou_jobs(days):
    output = "*************杭州市属start**************\n"
    url = 'http://hrss.hangzhou.gov.cn/module/xxgk/search.jsp'
    html = requests_utils.start_request(url,
                                        params={
                                            'infotypeId': 'HZRS030803',
                                            'jdid': '3163',
                                            'divid': 'div1229125915'
                                        },
                                        request_type=1)
    if html is None:
        output = output + '网页请求失败'
    else:
        output = output + parse_and_output(days, html, url)
    print(output + "*************杭州市属end**************\n")


def parse_and_output(days, html, url):
    local_time = datetime.now()
    soup = BeautifulSoup(html, 'lxml')
    dates = soup.find_all(string=re.compile(r'\d{4}-\d{2}-\d{2}'))
    a_tags = soup.find_all("a", target="_blank")
    max_len = max(len(dates), len(a_tags))
    result = ''
    interval_days = -1
    if True:
        for i in range(max_len):
            date = dates[i]
            if date is not None:
                item_date = datetime.strptime(date, "%Y-%m-%d")
                interval_days = (local_time - item_date).days
                if interval_days >= days:
                    continue
            else:
                continue
            a = a_tags[i]
            title = a.get('title')
            if not text_filter(title):
                result = result + date + ',' + title + ',link=' + a.get('href') + '\n'
    if interval_days < days:
        result = f"{result}最近{days}天杭州市属岗位发布较多，待续---> {url}\n"
    elif len(result) == 0:
        result = f"最近{days}天没有岗位发布\n"
    return result


def text_filter(text):
    return text is None or text.find('公示') > 0 or text.find('拟聘用') > 0
