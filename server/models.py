from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)


class Book(models.Model):
	def __str__(self):
		if self.title is None:
			return 'None'
		else:
			return self.title

	objects = models.Manager()
	title = models.CharField(max_length=256, blank=True, null=True)
	authors = models.CharField(max_length=256, blank=True, null=True)
	year = models.CharField(max_length=10, blank=True, null=True)
	edition = models.CharField(max_length=10, blank=True, null=True)

	def checkout(self, user, first_name, last_name):
		# Check if the latest transaction has been checked back in
		if not self.transaction_set.order_by('-checkout')[0].is_active():
			# Add a new one and check them out
			t = self.transaction_set.create(
				book=self,
				authorizer=user,
				first_name=first_name,
				last_name=last_name,
				checkout=datetime.now,
			)
			t.save()
			return t
		return None

	def checkin(self):
		# Check if the latest transaction has NOT been checked back in
		t = self.transaction_set.order_by('-checkout')[0]
		if t.is_active():
			t.checkin = datetime.now()
			return t
		return None


class Transaction(models.Model):
	def __str__(self):
		res = ''
		if self.book.title is None:
			res += 'None: '
		else:
			res += self.title + ': '
		return res
	objects = models.Manager()
	book = models.ForeignKey(
		Book,
		blank=True,
		null=True,
		on_delete=models.CASCADE
	)
	authorizer = models.ForeignKey(
		User,
		blank=True,
		null=True,
		on_delete=models.CASCADE
	)
	first_name = models.CharField(max_length=256, blank=True, null=True)
	last_name = models.CharField(max_length=256, blank=True, null=True)
	checkout = models.DateTimeField(blank=True, null=True)
	checkin = models.DateTimeField(blank=True, null=True)

	def is_active(self):
		if self.checkout is not None and self.checkin is None:
			return True
		return False
