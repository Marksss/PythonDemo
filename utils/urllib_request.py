# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import test

from urllib import request, parse
import ssl
import json
import xlwt


def fetch_data():
    context = ssl.create_default_context()
    url = 'http://api.kaiba315.com.cn/sc/service/activity/manage/activity/licenseLottery/getLotteryApplications'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'kb_cid': 'baa3bd70c1b011ebb10e259eaaf3e8b7',
        'kb_cnl': 201,
        'kb_do': 'Android',
        'kb_ep': 201,
        'kb_os': 'Android-Web',
        'kb_sid': 9,
        'kb_tkn': 'eyJhbGciOiJFUzI1NiJ9'
                  '.eyJqdGkiOiI0MTIxNTcwIiwic3ViIjoiMTEiLCJpYXQiOjE2MjI0MjQ5OTQsImV4cCI6MTYyMjQ0NjU5NH0'
                  '.jP4J8rQazyY6nPhJJw-a0txEWOBxy_TiFT2lVXsCasdN3RtXVY8H1mxtTUJoQHUAMZv2pXSc3JVl_9uDXWNMfQ',
        'kb_uid': 4121570,
        'Origin': 'https://page.kaiba315.com.cn',
        'Referer': 'https://page.kaiba315.com.cn/actionMap/list?id=6039b047335f830b4e117270&userId=4121570&token'
                   '=eyJhbGciOiJFUzI1NiJ9'
                   '.eyJqdGkiOiI0MTIxNTcwIiwic3ViIjoiMTEiLCJpYXQiOjE2MjI0MjQ5OTQsImV4cCI6MTYyMjQ0NjU5NH0'
                   '.jP4J8rQazyY6nPhJJw-a0txEWOBxy_TiFT2lVXsCasdN3RtXVY8H1mxtTUJoQHUAMZv2pXSc3JVl_9uDXWNMfQ&siteId=9',
        'Sec-Fetch-Mode': 'cors',
        'Cookie': 'sc=3817c18b6d215e538207df7dc07882d5',
        'User-Agent': 'Mozilla/5.0(Linux;Android 10;Pixel 2 Build/QQ2A.200501.001.B3; wv) AppleWebKit/537.36(KHTML, '
                      'like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36 kb_android kb_dsbridge_android '
    }
    dict2 = {
        'page': 1,
        'pageSize': 2000
    }
    data = bytes(parse.urlencode(dict2), 'utf-8')
    req = request.Request(url, data=data, headers=headers, method='POST')
    response = request.urlopen(req, context=context)
    return response.read().decode('utf-8')


def parse_data(raw_data):
    json_obj = json.loads(raw_data)
    applicants = []
    for item in json_obj['data']:
        if item.__contains__('user'):
            if item['user'].__contains__('userName'):
                user_name = item['user']['userName']
            else:
                user_name = ''
            if item['user'].__contains__('mobile'):
                user_mobile = item['user']['mobile']
            else:
                user_mobile = ''
        else:
            user_name = ''
            user_mobile = ''
        applicants.append({
            'userName': user_name,
            'userMobile': user_mobile,
            'applicantName': item['applicantName'],
            'lotteryNo': item['lotteryNo'],
            'mobile': item['mobile']
        })
    return applicants


def write_excel(data):
    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet("My new Sheet")
    data.insert(0, {
        'userName': '开吧用户昵称',
        'userMobile': '开吧用户电话',
        'applicantName': '报名姓名',
        'lotteryNo': '编号',
        'mobile': '报名电话'
    })
    for row, applicant in enumerate(data):
        worksheet.write(row, 0, applicant['userName'])
        worksheet.write(row, 1, applicant['userMobile'])
        worksheet.write(row, 2, applicant['applicantName'])
        worksheet.write(row, 3, applicant['lotteryNo'])
        worksheet.write(row, 4, applicant['mobile'])
    workbook.save("C:/Users/SXL/Desktop/摇号报名列表.xls")
    print('success')


rawData = fetch_data()
parsed_data = parse_data(rawData)
write_excel(parsed_data)
