# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as BS
from mechanize import Browser
from time import sleep

def scrape_words():

    word_list = []

    br = Browser()

    # Ignore robots.txt. Do not do this without thought and consideration.
    br.set_handle_robots(False)

    # Don't add Referer (sic) header
    br.set_handle_referer(False)

    # Don't handle Refresh redirections
    br.set_handle_refresh(False)

    # Setting the user agent as firefox
    br.addheaders = [('User-agent', 'Chrome'), ('Accept', '*/*')]

    base_url = 'http://masterrussian.com/vocabulary/common_nouns'

    # Crawl through pages
    for page in range(1,2):

        # Stagger Requests to keep Server Happy
        sleep(1)

        # Compose Page Url
        if page == 1:
            first_page = base_url + '.htm'
            br.open(first_page)
        else:
            next_page = base_url + '_' + str(page) + '.htm'
            br.open(next_page)

        # Parse and Collect Words on Page
        soup = BS(br.response().read(), 'html.parser')
        tr_set = soup.findAll("tr", { "class" : "rowFirst" })
        tr_set.extend(soup.findAll("tr", {"class": "rowSecond"}))
        for tr in tr_set:
            children = tr.findChildren()

            # Differentiate between table rows that do/do not contain a link
            if 'href' in str(tr):
                word = [word_info.contents for index, word_info in enumerate(children) if index > 1]

                # A word list should only contain three entries: noun, translation, gender
                if len(word) == 3:
                    word_list.append(word)
            else:
                word = [word_info.contents for index, word_info in enumerate(children) if index > 0]
                if len(word) == 3:
                    word_list.append(word)

        print 'Collected ' + str(len(word_list)) + '/500 words'

    return word_list
