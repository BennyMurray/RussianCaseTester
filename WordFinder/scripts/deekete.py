# -*- coding: utf-8 -*-
from scrape_words import scrape_words
from bs4 import BeautifulSoup as BS
from mechanize import Browser
from declension_parser import declension_parser
from time import sleep
import re

# word_list = scrape_words()
# for word in word_list:
#     print word[0]

# SUBMITS SEARCH
#
# list = scrape_words()
# word_list = []
# for item in list:
#     word_list.append(item[0][0])

# for i in word_list:
#     print i
#

# for word in word_list:
#     sleep(1)
#     br = Browser()
#     br.set_handle_robots(False)
#     br.open("http://www.multitran.ru/c/m.exe?a=1&SHL=2")
#     br.select_form('translation')
#     br.form['s'] = word.encode('utf8')
#     print word
#     response1 = br.submit()
#     soup = BS(response1, "html.parser")
#     response2 = br.follow_link(nr=13)
#     soup2 = BS(response2, "html.parser")
#     string = soup2.text
#     declension_parser(string)


# def source_declension(word):
#     print word
#     sleep(1)
#     br = Browser()
#     br.set_handle_robots(False)
#     br.open("http://www.multitran.ru/c/m.exe?a=1&SHL=2")
#     br.select_form('translation')
#     br.form['s'] = word.encode('utf8')
#     response1 = br.submit()
#     response2 = br.follow_link(nr=13)
#     soup2 = BS(response2, "html.parser")
#     string = soup2.text
#     x = declension_parser(string)
#     if len(x) != 12:
#         return word, 'We have a problem'
#     else:
#         return word, 'All good here'
#
#


br = Browser()
br.set_handle_robots(False)
br.open("http://www.multitran.ru/c/m.exe?a=118&t=15491_2_1")
br.select_form(nr=0)
br.form['s'] = 'спина'
response = br.submit()
soup = BS(response, "html.parser")
x = declension_parser(soup.text)
for i in x:
    print i

# print test(u'Москва')
# print test(u'спина ')
#
#
