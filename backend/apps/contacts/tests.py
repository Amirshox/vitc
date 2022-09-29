from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory, APITestCase

from rest_framework_simplejwt.tokens import RefreshToken

from ..users.models import User


class ContactTest(APITestCase):

    def setUp(self) -> None:
        self.username = 'i'
        self.password = '1'
        user = User(username=self.username)
        user.set_password(self.password)
        user.save()

    @property
    def bearer_token(self):
        user = User.objects.get(id=1)

        refresh = RefreshToken.for_user(user)
        return {"HTTP_AUTHORIZATION": f'Bearer {refresh.access_token}'}

    def test_contact_create(self):
        data = {
            'full_name': "abc",
            "phone_number": "998123456789",
            "email": "a@gmail.com",
            "gender": "male",
            "tags": []
        }
        response = self.client.post(reverse("contacts:contact-list"), data=data, **self.bearer_token)
        self.assertEqual(201, response.status_code)

    def test_contact_list_without_auth(self):
        response = self.client.get(reverse("contacts:contact-list"))
        self.assertEqual(401, response.status_code)

    def test_contact_list(self):
        response = self.client.get(reverse("contacts:contact-list"), **self.bearer_token)
        self.assertEqual(200, response.status_code)
