# -*- coding: utf-8 -*-
import re

string = 'рука (Именительный падеж'.decode('utf-8')
string2 = 'hi im a string'
print re.findall(u"(?u)\w+ \(Именительный падеж", string)[0].split()[0]




# (?u)\w+ \(Именительный падеж