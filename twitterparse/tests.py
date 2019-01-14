from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Twitterparse
from .serializers import TwitterparseSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_user(user="", ):
        if user != "":
            client.objects.create(user=name)

    def setUp(self):
        # add test data
        self.create_user("Katherine")



class GetAllTimelineTest(BaseViewTest):

    def test_get_all_timelines(self):
        """
        This test ensures that all timelines added in the setUp method
        exist when we make a GET request to the twitterparse/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("timelines", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = User.objects.all()
        serialized = TwitterparseSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
