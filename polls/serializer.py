from rest_framework import serializers
from .models import maktab, xonalar


class maktabSerializer(serializers.ModelSerializer):
    class Meta:
        model=maktab
        fields = ('name', 'oquvchilar_soni')


class xonalarSerializer(serializers.ModelSerializer):
    class Meta:
        model=xonalar
        fields=('xonanomi', 'nechikishiligi')