from django.test import TestCase, Client
from django.urls import reverse
from photolibrary.models import *
import json


class TestViews(TestCase):
	def setUp(self):
		self.client = Client()
		self.user = User.objects.create_user('mutebialvinalvienzo@gmail.com','alvinmutebi','Alvin','Mutebi','hellowprds')
	
	def test_login_view(self):
		self.client.login(email='mutebialvinalvienzo@gmail.com', password='hellowprds')
		response = self.client.get(reverse('login'))
		self.assertEquals(response.status_code, 200)


	def test_logout_view(self):
		self.client.logout()
		response = self.client.get(reverse('login'))
		self.assertEquals(response.status_code, 200)



	def expand_image_view(self):
		response = self.client.get(reverse('photo'), args=['some-flug'])
		self.assertEquals(response.status_code, 200)


	def create_photo_view(self):
		response = self.client.post(reverse('createPhoto'))
		self.assertEquals(response.status_code, 200)



