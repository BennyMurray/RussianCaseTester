# -*- coding: utf-8 -*-
import re

def parse_declensions(string):
    
    # Singular
    nominative_singular = re.findall(u"(?u)\w+ \(Именительный падеж единственного", string)[0].split()[0]
    genitive_singular = re.findall(u"(?u)\w+ \(Родительный падеж единственного", string)[0].split()[0]
    dative_singular = re.findall(u"(?u)\w+ \(Дательный падеж единственного", string)[0].split()[0]
    accusative_singular = re.findall(u"(?u)\w+ \(Винительный падеж единственного", string)[0].split()[0]
    prepositional_singular = re.findall(u"(?u)\w+ \(Творительный падеж единственного", string)[0].split()[0]
    instrumental_singular = re.findall(u"(?u)\w+ \(Предложный падеж единственного", string)[0].split()[0]

    # Plural
    try:
        nominative_plural = re.findall(u"(?u)\w+ \(Именительный падеж множественного", string)[0].split()[0]
        genitive_plural = re.findall(u"(?u)\w+ \(Родительный падеж множественного", string)[0].split()[0]
        dative_plural = re.findall(u"(?u)\w+ \(Дательный падеж множественного", string)[0].split()[0]
        accusative_plural = re.findall(u"(?u)\w+ \(Винительный падеж множественного", string)[0].split()[0]
        prepositional_plural = re.findall(u"(?u)\w+ \(Творительный падеж множественного", string)[0].split()[0]
        instrumental_plural = re.findall(u"(?u)\w+ \(Предложный падеж множественного", string)[0].split()[0]

    except IndexError:
        nominative_plural = '-'
        genitive_plural = '-'
        dative_plural = '-'
        accusative_plural = '-'
        prepositional_plural = '-'
        instrumental_plural = '-'

    # Accommodate for nouns with two declensions
    if ',' in prepositional_singular:
        prepositional_singular = prepositional_singular.split(',')[0]

    case_list = [nominative_singular, accusative_singular, dative_singular, genitive_singular, prepositional_singular, instrumental_singular, nominative_plural, accusative_plural, dative_plural, genitive_plural, prepositional_plural, instrumental_plural]
    return case_list

