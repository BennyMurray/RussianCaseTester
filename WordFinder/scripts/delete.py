# -*- coding: utf-8 -*-
import re

text = u'Результаты морфологического анализа спина ж.род cheese'
control_text = u'аде (Именительный падеж единственного'
gender = re.findall(u"(?u)\w\.род", text)
control = re.findall(u"(?u)\w+ \(Именительный падеж единственного", control_text)

for i in gender:
    print i,


print '\n----------------------'

for x in control:
    print x
