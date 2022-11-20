from django.test import SimpleTestCase
from django.urls import reverse, resolve
from photolibrary.views import *
from django.contrib.auth.views import *

class TestUrls(SimpleTestCase):

	def test_login_url_is_resolved(self):
		url = reverse('login')
		self.assertEquals(resolve(url).func, loginUser)

	def test_register_url_is_resolved(self):
		url = reverse('register')
		self.assertEquals(resolve(url).func, registerUser)

	def test_logout_url_is_resolved(self):
		url = reverse('logout')
		self.assertEquals(resolve(url).func, logoutUser)

	def test_home_url_is_resolved(self):
		url = reverse('home')
		self.assertEquals(resolve(url).func, home)

	def test_createphoto_url_is_resolved(self):
		url = reverse('createPhoto')
		self.assertEquals(resolve(url).func, createPhoto)

	def test_photo_url_is_resolved(self):
		url = reverse('photo', args=['some-slug'])
		self.assertEquals(resolve(url).func, expandImage)

	def test_password_reset_url_is_resolved(self):
		url = reverse('reset_password')
		self.assertEquals(resolve(url).func.view_class, PasswordResetView)

	def test_reset_password_sent_url_is_resolved(self):
		url = reverse('password_reset_done')
		self.assertEquals(resolve(url).func.view_class, PasswordResetDoneView)

	def test_reset_password_confrim_url_is_resolved(self):
		url = reverse('password_reset_confirm', args=['some-slug','some-slug'])
		self.assertEquals(resolve(url).func.view_class, PasswordResetConfirmView)

	def test_reset_password_complete_url_is_resolved(self):
		url = reverse('password_reset_complete')
		self.assertEquals(resolve(url).func.view_class, PasswordResetCompleteView)




	





