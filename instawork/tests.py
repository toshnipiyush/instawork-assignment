import json
from unittest import TestCase

from django.test import Client
from rest_framework import status

from instawork.models import TeamMember


class BaseTestCase(TestCase):
    def setUp(self):
        """
        Setting up test cases
        """
        super(BaseTestCase, self).setUp()
        self.mock_data = {
            "first_name": "Piyush",
            "last_name": "Toshniwal",
            "phone_number": "8754517885",
            "email": "toshnipiyush@gmail.com",
            "role": 0
        }
        self.client = Client()

    def _get(self, url):
        """
        Makes get request to the specified url
        """
        return self.client.get(url)

    def _post(self, url, data=None, data_format='application/json'):
        """
        Makes post request with data to the specific urls
        """
        return self.client.post(url, data=data, content_type=data_format)

    def _patch(self, url, data=None, data_format='application/json'):
        """
        Makes post request with data to the specific urls
        """
        return self.client.patch(url, data=data, content_type=data_format)

    def _delete(self, url, data=None, data_format='application/json'):
        """
        Makes post request with data to the specific urls
        """
        return self.client.delete(url, data=data, content_type=data_format)


class TestTeamMember(BaseTestCase):

    def test_create_team_member(self):
        response = self._post('/api/v1/users/', data=self.mock_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(response.content), {
            "id": 1,
            "first_name": "Piyush",
            "last_name": "Toshniwal",
            "phone_number": "8754517885",
            "email": "toshnipiyush@gmail.com",
            "role": 0
        })
        self.assertEqual(TeamMember.objects.count(), 1)

    def test_edit_team_member(self):
        data = {
            "phone_number": "8754517883",
            "role": 1
        }
        response = self._patch('/api/v1/users/1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {
            "id": 1,
            "first_name": "Piyush",
            "last_name": "Toshniwal",
            "phone_number": "8754517883",
            "email": "toshnipiyush@gmail.com",
            "role": 1
        })
        self.assertEqual(TeamMember.objects.count(), 1)

    def test_get_all_team_member(self):
        response = self._get('/api/v1/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(response.content)), 1)
        self.assertEqual(json.loads(response.content), [{
            "id": 1,
            "first_name": "Piyush",
            "last_name": "Toshniwal",
            "phone_number": "8754517883",
            "email": "toshnipiyush@gmail.com",
            "role": 1
        }])
        self.assertEqual(TeamMember.objects.count(), 1)

    def test_get_single_team_member(self):
        response = self._get('/api/v1/users/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {
            "id": 1,
            "first_name": "Piyush",
            "last_name": "Toshniwal",
            "phone_number": "8754517883",
            "email": "toshnipiyush@gmail.com",
            "role": 1
        })

    def test_delete_team_member(self):
        self._post('/api/v1/users/', data=self.mock_data)
        response = self._delete('/api/v1/users/2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(TeamMember.objects.count(), 1)

    def test_get_single_team_member_with_invalid_id(self):
        response = self._get('/api/v1/users/5/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(json.loads(response.content), {"detail": "Not found."})

    def test_delete_team_member_with_invalid_id(self):
        response = self._delete('/api/v1/users/5/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(json.loads(response.content), {"detail": "Not found."})
