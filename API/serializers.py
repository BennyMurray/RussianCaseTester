from WordFinder.models import Word
from rest_framework import serializers


class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ('spelling', 
                  'translation', 
                  'gender', 
                  'nominative_singular', 
                  'accusative_singular',
                  'genitive_singular',
                  'dative_singular',
                  'prepositional_singular',
                  'instrumental_singular',
                  'nominative_plural',
                  'accusative_plural',
                  'genitive_plural',
                  'dative_plural',
                  'prepositional_plural',
                  'instrumental_plural',
                  )