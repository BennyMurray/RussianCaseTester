# -*- coding: utf-8 -*-
import re

def parse_gender(text):
    gender = re.findall(u"(?u)\w\.род", text)
    try:
        return gender[0]
    except IndexError:
        return 'gender not defined'