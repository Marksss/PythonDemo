# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import test

from urllib import request, parse
import ssl

context = ssl.create_default_context()
url = 'https://api.kaiba315.com.cn/activity/actionMap/getActionMapById'
headers = {
    # 假装自己是浏览器
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
    'User-Agent': 'Mozilla/5.0(Linux;Android 10;Pixel 2 Build/QQ2A.200501.001.B3; wv) AppleWebKit/537.36(KHTML, '
                  'like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36 kb_android kb_dsbridge_android '
}
dict2 = {
    'id': '6039b047335f830b4e117270'
}
data = bytes(parse.urlencode(dict2), 'utf-8')
req = request.Request(url, data=data, headers=headers, method='POST')
response = request.urlopen(req, context=context)
print(response.read().decode('utf-8'))
