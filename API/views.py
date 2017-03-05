from random import sample

from WordFinder.models import Word
from.serializers import WordSerializer
from rest_framework import generics

class WordList(generics.ListAPIView):

    serializer_class = WordSerializer

    def get_queryset(self):
        excluded_genders = self.kwargs['excluded_genders'].split('x-')

        #cache this or does it automatically cache?
        id_pool = Word.objects.values_list('id', flat=True).exclude(gender__in=excluded_genders)
        random_ids = sample(id_pool, 10)
        return Word.objects.filter(id__in=random_ids)

