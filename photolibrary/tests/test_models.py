from django.test import TestCase
from photolibrary.models import *

class TestModels(TestCase):
	
	def setUp(self):
		self.user1 = User.objects.create(
			username='alvinmutebi',
			first_name='Alvin',
			last_name="Mutebi",
			email="mutebialvinalvienzo@gmail.com",
			is_staff=False,
			is_active=True,
			date_joined='2022-11-19 19:06:28'
			)


	def test_user_username(self):
		self.assertEquals(self.user1.username, 'alvinmutebi')

	def test_user_fullname(self):
		self.assertEquals(self.user1.first_name, 'Alvin')
		self.assertEquals(self.user1.last_name, 'Mutebi')


	def test_image_to_upload(self):
		self.photo1 = OurPhoto.objects.create(
			image='static/images/1865378.jpg',
			title='Robots',
			description='hellothere'
			)
		self.assertEquals(self.photo1.image, 'static/images/1865378.jpg')


	def test_title(self):
		self.photo1 = OurPhoto.objects.create(
			image='static/images/1865378.jpg',
			title='Robots',
			description='hellothere'
			)
		self.assertEquals(self.photo1.title, 'Robots')

	def test_description(self):
		self.photo1 = OurPhoto.objects.create(
			image='static/images/1865378.jpg',
			title='Robots',
			description='hellothere'
			)
		self.assertEquals(self.photo1.description, 'hellothere')






