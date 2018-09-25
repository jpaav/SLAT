from rest_framework import serializers

from .models import *


class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = ('pk', 'title', 'authors', 'year', 'edition')
		read_only_fields = ('pk',)


class TransactionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transaction
		fields = ('pk', 'first_name', 'last_name', 'checkout', 'checkin')
		read_only_fields = ('pk',)

