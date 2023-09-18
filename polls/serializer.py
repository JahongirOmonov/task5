from rest_framework import serializers
from .models import maktab, xonalar
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User 


class maktabSerializer(serializers.ModelSerializer):
    class Meta:
        model=maktab
        fields = ('name', 'oquvchilar_soni', 'user')

    def create(self, validated_data):
        validated_data['user']=get_object_or_404(User, username=self.context['request'].user)
        return super(maktabSerializer, self).create(validated_data)


class xonalarSerializer(serializers.ModelSerializer):
    class Meta:
        model=xonalar
        fields=('xonanomi', 'nechikishiligi', 'user')

    def create(self, validated_data):
        validated_data['user']=get_object_or_404(User, username=self.context['request'].user)
        return super(xonalarSerializer, self).create(validated_data)