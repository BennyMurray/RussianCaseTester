from WordFinder.models import Word
from rest_framework import serializers


class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ('spelling', 'translation', 'gender')