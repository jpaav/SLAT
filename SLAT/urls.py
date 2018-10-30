"""SLAT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.urls import include, path
	2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as rest_auth_views

from server import api

server_patterns = [
	path('admin/', admin.site.urls),
	path('library/', include('server.urls'), name='library'),
	path('', RedirectView.as_view(url='/library/')),
	path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
	path('logout/', LogoutView.as_view(), {'next_page': '/accounts/logout_lander'}, name='logout'),
]

api_patterns = [
	path('api/books/', api.BookList.as_view()),
	path('api/book/<int:book_pk>', api.Book.as_view()),
	path('api/book/<int:book_pk>/transactions/', api.BookTransactions.as_view()),
	# path('api/book/<int:pk>/latest_transaction/', api.BookTransactions.as_view()),
	path('api/transaction/', api.Transaction.as_view()),
	path('api-token-auth/', rest_auth_views.obtain_auth_token),
]

urlpatterns = server_patterns + api_patterns
urlpatterns = format_suffix_patterns(urlpatterns)
