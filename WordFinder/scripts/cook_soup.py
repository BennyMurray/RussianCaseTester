# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as BS
from mechanize import Browser
from time import sleep

def cook_soup(word):

    # Stagger Request
    sleep(1)

    # Search for passed word
    br = Browser()
    br.set_handle_robots(False)
    br.open("http://www.multitran.ru/c/m.exe?a=118&t=15491_2_1")
    br.select_form(nr=0)
    br.form['s'] = word.encode('utf8')
    response = br.submit()

    # Capture Text
    soup = BS(response, "html.parser")
    return soup.text


