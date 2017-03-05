# -*- coding: utf-8 -*-

from scrape_words import scrape_words
from cook_soup import cook_soup
from declension_parser import parse_declensions

from WordFinder.models import Word


def run():

    word_dict = scrape_words()
    for key, val in word_dict.items():
        spelling = key
        translation = val['translation']
        gender = val['gender'].upper()
        soup = cook_soup(key)
        declension_list = parse_declensions(soup)

        # Create model instance
        w, created = Word.objects.get_or_create(spelling=spelling, translation=translation,
                                                gender=gender,lexical_category='NOUN', nominative_singular=declension_list[0],
                                                accusative_singular=declension_list[1], dative_singular=declension_list[2],
                                                genitive_singular=declension_list[3], prepositional_singular=declension_list[4],
                                                instrumental_singular=declension_list[5], nominative_plural=declension_list[0],
                                                accusative_plural=declension_list[1], dative_plural=declension_list[2],
                                                genitive_plural=declension_list[3], prepositional_plural=declension_list[4],
                                                instrumental_plural=declension_list[5])

        print ("- Word: {0}, Created: {1}".format(str(w), str(created)))


