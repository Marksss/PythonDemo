import requests_utils
from datetime import datetime
from bs4 import BeautifulSoup


def get_college_jobs(days):
    output = ''
    for i in range(1, 5):
        url = f'http://www.gaoxiaojob.com/zhaopin/gaoxiao/zhejiang/index_{i}.html'
        html = requests_utils.start_request(url)
        if html is None:
            if len(output) > 0:
                output = f'{output}\npage({i})网页请求失败'
            else:
                output = '网页请求失败'
            break
        else:
            result = parse_and_output(days, html)
            output = output + result[0]
            if not result[1]:
                break
    if len(output) == 0:
        output = f"最近{days}天没有岗位发布\n"
    print("*************浙江高校start**************\n" + output +
          "*************浙江高校end**************\n")


def parse_and_output(days, html):
    interval_days = -1
    local_time = datetime.now()
    soup = BeautifulSoup(html, 'lxml')
    item_tag = soup.find("span", class_="ltitle")
    result = ''
    while item_tag is not None:
        date_no_year = item_tag.find('small').string[1:-1]
        date = f'{local_time.year}.{date_no_year}'
        if date is not None:
            item_date = datetime.strptime(date, "%Y.%m.%d")
            interval_days = (local_time - item_date).days
            if interval_days < days:
                title = item_tag.a.string
                link = item_tag.a.get('href')
                if not text_filter(title) and link is not None:
                    result = f'{result}{date},{title[1:]},link={link}\n'
        item_tag = item_tag.find_next("span", class_="ltitle")
    return [result, interval_days < days]


def text_filter(text):
    return text is None or text.find('浙江大学') > 0 or text.find('西湖大学') > 0
