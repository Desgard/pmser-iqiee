#!/usr/bin/env python

import requests
from issue import Issue
from config import key_dic

xml_url = "http://pms.qiyi.domain/sr/jira.issueviews:searchrequest-xml/temp/SearchRequest.xml"
find_name = "duanhaoyu"

params = {
    'jqlQuery': 'assignee in (%r) ORDER BY created DESC' % find_name,
    'tempMax': '1000',
}

cookie = 'JSESSIONID=8DB196651065C1561CF2288807BCE054; atlassian.xsrf.token=BIM2-2D98-FCIE-BUVL|4d566777d0238c5f80370558535bdad7d2b7859a|lin'

headers = {
    'Pragma': 'no-cache',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://pms.qiyi.domain/browse/TVGUOBUG-2148?jql=assignee in (%r) ORDER BY created DESC' % find_name,
    'Connection': 'keep-alive',
    'Cache-Control': 'no-cache',
    'cookie': cookie,
}


r = requests.get(xml_url, headers = headers, params = params)

xml_txt = r.text
# print(xml_txt)

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

root = ET.fromstringlist(xml_txt)

res = []

# Catch all issue about me
for item in root.iter('item'):
    dict = {}
    for key in key_dic:
        iss_item = item.find(key)
        if iss_item is None:
            continue
        else:
            dict[key] = iss_item.text
    res.append(dict)

# print(res)
# To translate mine class
issues_res = []

for issue_dic in res:
    issue = Issue(issue_dic)
    issues_res.append(issue)

for issue in issues_res:
    print(issue)
