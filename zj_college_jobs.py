import requests_utils
from datetime import datetime
from bs4 import BeautifulSoup


def get_college_jobs(days):
    output = "*************浙江高校start**************\n"
    url = 'http://www.gaoxiaojob.com/zhaopin/gaoxiao/zhejiang/'
    html = requests_utils.start_request(url)
    if html is None:
        output = output + '网页请求失败'
    else:
        output = output + parse_and_output(days, html, url)
    print(output + "*************浙江高校end**************\n")


def parse_and_output(days, html, url):
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
                    result = result + date + ',' + title[1:] + ',link=' + link + '\n'
        item_tag = item_tag.find_next("span", class_="ltitle")
    if interval_days < days:
        result = f"{result}最近{days}天高校岗位发布较多，待续---> {url}\n"
    elif len(result) == 0:
        result = f"最近{days}天没有岗位发布\n"
    return result


def text_filter(text):
    return text is None or text.find('浙江大学') > 0 or text.find('西湖大学') > 0
