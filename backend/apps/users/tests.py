from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory, APITestCase

from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


class UserTest(APITestCase):

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

    def test_user_create(self):
        data = {
            'username': "admin",
            "password": "1"
        }
        response = self.client.post(reverse("users:user-list"), data=data)
        self.assertEqual(201, response.status_code)

    def test_contact_detail(self):
        response = self.client.get(reverse("users:user-detail", args=[1]), **self.bearer_token)
        self.assertEqual(200, response.status_code)
