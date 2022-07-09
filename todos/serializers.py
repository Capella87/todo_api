from rest_framework import serializers
from todos import models

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Todo
        fields = [
            'id',
            'title',
            'isstarred',
            'description',
        ]

