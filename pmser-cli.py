#! /usr/bin/env python

import argparse
import pmserpac

parser = argparse.ArgumentParser(description = "To build the weekly report quickly!")

parser.add_argument('-u', '--user', help = 'Filter the item of this user.')
parser.add_argument('-w', '--week', help = 'Only show this week report.', action = 'store_true')
parser.add_argument('-a', '--all', help = '[Default] Show all issues about the user.', action = 'store_true')

args = parser.parse_args()

res = []

if args.user:
    find_user = args.user
    pmserpac.configure_net(find_user)
    xml_txt = pmserpac.request_net()
    res = pmserpac.analysis2list(xml_txt)

if args.week:
    for issue in res:
        if issue.is_in_week():
            print(issue)

else:
    for issue in res:
        print(issue)
