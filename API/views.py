from random import sample

from WordFinder.models import Word
from rest_framework import viewsets
from.serializers import WordSerializer


class WordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    num_entities = Word.objects.all().count()
    rand_entities = sample(range(num_entities), 10)
    queryset = Word.objects.filter(id__in=rand_entities)

    serializer_class = WordSerializer