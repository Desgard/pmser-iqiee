from config import key_dic
from datetime import datetime
from dateutil import parser

class Issue:
    title = ""
    link = ""
    description = ""
    summary = ""
    type = ""
    summary = ""
    priority = ""
    status = ""
    resolution = ""
    assignee = ""
    reporter = ""
    version = ""
    fixVersion = ""
    component = ""
    created = ""
    updated = ""
    resolved = ""
    resolved_time = datetime.now()

    def __init__(self, dic = {}):
        if type(dic) != dict:
            return
        for key in key_dic:
            if dic.__contains__(key) and hasattr(self, key):
                setattr(self, key, dic[key])

        try:
            self.resolved_time = parser.parse(self.resolved)
        except(ValueError):
            pass


    def __str__(self):
        time = self.resolved_time.strftime("%y-%b-%d")
        title = self.title
        return "%r: %r" % (time, title)

    def is_in_week(self):
        now = datetime.today()
        # print(now.strftime("%W"), self.resolved_time.strftime("%W"))
        return now.strftime("%W") == self.resolved_time.strftime("%W")

    def is_complete(self):
        return True

    def is_running(self):
        if self.status == "进行中":
            return True
        return False

class Comment:
    id = ""
    author = ""
    body = ""
