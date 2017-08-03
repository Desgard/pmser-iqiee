#! /usr/bin/env python

import argparse
import pmserpac

parser = argparse.ArgumentParser(description = "To build the weekly report quickly!")

parser.add_argument('-u', '--user', help = 'Filter the item of this user.')
parser.add_argument('-w', '--week', help = 'Only show this week report.')

args = parser.parse_args()

if args.user:
    find_user = args.user
    pmserpac.configure_net(find_user)
    xml_txt = pmserpac.request_net()
    res = pmserpac.analysis2list(xml_txt)
    for issue in res:
        print(issue)



