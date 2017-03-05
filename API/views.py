from random import sample

from WordFinder.models import Word
from.serializers import WordSerializer
from rest_framework import generics

class WordList(generics.ListAPIView):

    serializer_class = WordSerializer

    def get_queryset(self):
        num_entities = Word.objects.all().count()
        rand_entities = sample(range(num_entities), 10)
        return Word.objects.filter(id__in=rand_entities)

