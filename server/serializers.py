from rest_framework import serializers

from .models import *


class BookSerializer(serializers.ModelSerializer):
	checked_out = serializers.CharField(source='is_active')

	class Meta:
		model = Book
		fields = ('pk', 'title', 'authors', 'year', 'edition', 'checked_out')
		read_only_fields = ('pk', 'checked_out')


class TransactionSerializer(serializers.ModelSerializer):
	checked_out = serializers.CharField(source='is_active')

	class Meta:
		model = Transaction
		fields = ('pk', 'first_name', 'last_name', 'checkout', 'checkin', 'checked_out', 'authorizer')
		read_only_fields = ('pk', 'checked_out')

