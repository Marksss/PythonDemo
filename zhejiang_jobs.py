import requests_utils
import re
from datetime import datetime


def get_zhejiang_jobs(days):
    output = "*************省属start**************\n"
    url = 'http://rlsbt.zj.gov.cn/col/col1443681/index.html'
    html = requests_utils.start_request(url)
    if html is None:
        output = output + '网页请求失败'
    else:
        output = output + parse_and_output(days, html, url)
    print(output + "*************省属end**************\n")


def parse_and_output(days, html, url):
    local_time = datetime.now()
    res = re.findall('<li style=.+</span><br></li>]]>', html)
    interval_days = -1
    result = ''
    if len(res) == 0:
        result = '数据异常'
    else:
        for item in res:
            date = re.findall('<span class=\'.+\' style=".+">(.+)</span>', item)
            if len(date) > 0 and date[0] is not None:
                item_date = datetime.strptime(date[0], "%Y-%m-%d")
                interval_days = (local_time - item_date).days
                if interval_days >= days:
                    continue
            else:
                continue
            text = re.findall('target="_blank">(.+)</a>', item)
            if len(text) == 0 or text_filter(text[0]):
                continue
            link = re.findall('href=\'(.+)\' class', item)
            if len(link) > 0:
                result = result + date[0] + ',' + text[0] + ',link=http://rlsbt.zj.gov.cn' + link[0] + '\n'
    if interval_days < days:
        result = f"{result}最近{days}天省属岗位发布较多，待续---> {url}\n"
    elif len(result) == 0:
        result = f"最近{days}天没有岗位发布\n"
    return result


def text_filter(text):
    return text is None or text.find('公示') > 0 or text.find('拟聘用') > 0
