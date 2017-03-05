from django.db import models

class Word(models.Model):

    GENDER_CHOICES = (
        ('MASCULINE', 'masculine'),
        ('FEMININE', 'feminine'),
        ('NEUTER', 'neuter'),
    )

    LEXICAL_CATEGORY_CHOICES = (
        ('NOUN', 'noun'),
        ('ADJECTIVE', 'adjective'),
    )

    spelling = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)
    gender = models.CharField(max_length=8, choices=GENDER_CHOICES)
    lexical_category = models.CharField(max_length=9, choices=LEXICAL_CATEGORY_CHOICES)
    regular = models.BooleanField(default=True)
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

    def __unicode__(self):
        return self.spelling



