import requests
from issue import Issue
from config import key_dic

url = "http://pms.qiyi.domain/sr/jira.issueviews:searchrequest-xml/temp/SearchRequest.xml"
cookie = 'JSESSIONID=C059FB22D702EA0C3C98A07E7E68F5F0; atlassian.xsrf.token=BIM2-2D98-FCIE-BUVL|8810efc59a1966ed54bbd0794d5cb423d1f729be|lin'
params = {}
headers = {}

issue_res = []

def configure_net(find_name):
    global params
    global headers

    params = {
        'jqlQuery': 'assignee in (%r) ORDER BY created DESC' % find_name,
        'tempMax': '1000',
    }

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


def request_net(u = None, h = None, p = None):
    if u is None:
        global url
        u = url
    if h is None:
        global headers
        h = headers
    if p is None:
        global params
        p = params
    res = requests.get(u, headers = h, params = p)
    xml_txt = res.text
    return xml_txt


def analysis2list(xml_txt):
    try:
        import xml.etree.cElementTree as ET
    except:
        import xml.etree.ElementTree as ET
    try:
        root = ET.fromstringlist(xml_txt)
        res = []
        for item in root.iter('item'):
            dict = {}
            for key in key_dic:
                iss_item = item.find(key)
                if iss_item is None:
                    continue
                else:
                    dict[key] = iss_item.text
            res.append(dict)

        issue_res = []
        for issue_dic in res:
            issue = Issue(issue_dic)
            issue_res.append(issue)
        return issue_res
    except:
        print('analysis xml failure.')
        return None

