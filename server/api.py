from rest_framework import generics, authentication, permissions
from .serializers import *


class BookList(generics.ListCreateAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	authentication_classes = (authentication.TokenAuthentication,)
	permission_classes = (permissions.IsAuthenticated,)


class Book(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = BookSerializer
	authentication_classes = (authentication.TokenAuthentication,)
	permission_classes = (permissions.IsAuthenticated,)

	def get_object(self):
		pk = self.kwargs.get('book_pk')
		return Book.objects.get(pk=pk)


class BookTransactions(generics.ListCreateAPIView):
	serializer_class = TransactionSerializer
	authentication_classes = (authentication.TokenAuthentication,)
	permission_classes = (permissions.IsAuthenticated,)

	def get_queryset(self):
		book = self.request.GET.get('book_pk')
		if book is not None:
			return Transaction.objects.filter(book=book)
		else:
			return None

	def perform_create(self, serializer):
		return serializer.save(authorizer=self.request.user, checkout=datetime.now(), checkin=None)


class Transaction(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = TransactionSerializer
	authentication_classes = (authentication.TokenAuthentication,)
	permission_classes = (permissions.IsAuthenticated,)

	def get_object(self):
		pk = self.kwargs.get('pk')
		return Transaction.objects.get(pk=pk)