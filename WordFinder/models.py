from django.db import models

class Word(models.Model):

    GENDER_CHOICES = (
        ('MASCULINE', 'Masculine'),
        ('FEMININE', 'Feminine'),
        ('NEUTER', 'Neuter'),
    )

    LEXICAL_CATEGORY_CHOICES = (
        ('NOUN', 'Noun'),
        ('ADJECTIVE', 'Adjective'),
    )

    gender = models.CharField(max_length=8, choice=GENDER_CHOICES)
    lexical_category = models.CharField(max_length=9, choice=LEXICAL_CATEGORY_CHOICES)
    regular = models.BooleanField(required=True)
    nominative_singular = models.CharField(max_length=100)
    accusative_singular = models.CharField(max_length=100)
    dative_singular = models.CharField(max_length=100)
    genitive_singular = models.CharField(max_length=100)
    prepositional_singular = models.CharField(max_length=100)
    instrumental_singular = models.CharField(max_length=100)
    nominative_plural = models.CharField(max_length=100)
    accusative_plural = models.CharField(max_length=100)
    dative_plural = models.CharField(max_length=100)
    genitive_plural = models.CharField(max_length=100)
    prepositional_plural = models.CharField(max_length=100)
    instrumental_plural = models.CharField(max_length=100)



