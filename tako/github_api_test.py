#!/usr/bin/env python3

from github import Github
from pprint import pprint
import datetime


repo = Github().get_repo('ansible/ansible')

now = datetime.datetime.now()
last_report = now - datetime.timedelta(days=7)

pprint(now)
pprint(last_report)

help(repo)
for pull in repo.get_pulls(since=last_report,until=now):
    pprint(pull)

