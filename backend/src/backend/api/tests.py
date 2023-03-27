import json
from django.test import SimpleTestCase , Client
from django.urls import reverse
from .utils import get_mock_data, save_mock_data

class TaskTestCase(SimpleTestCase ):
    def setUp(self):
        self.client = Client()

    def assertSuccess(self, response, id=None):
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['success'], True)
        if id is not None:
            self.assertEqual(data['id'], id)

    def assertError(self, response):
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data.get('error'), None)
        self.assertEqual(data.get('success'), None)

    def test_add_task(self):
        # Test adding a new task
        url = reverse('add_task')
        data = {"title": "Test Task", "description": "This is a test task."}
        response = self.client.post(url, json.dumps(data), content_type='application/json')
        self.assertSuccess(response, id=1)

        # Test adding another task
        data = {"title": "Another Test Task", "completed": True}
        response = self.client.post(url, json.dumps(data), content_type='application/json')
        self.assertSuccess(response, id=2)

        # Test adding a task without a title
        data = {"description": "This task has no title."}
        response = self.client.post(url, json.dumps(data), content_type='application/json')
        self.assertError(response)

    def test_delete_task(self):
        # Test deleting a task
        url = reverse('delete_task', args=[1])
        response = self.client.delete(url)
        self.assertSuccess(response)

        # Test deleting a non-existent task
        response = self.client.delete(url)
        self.assertError(response)

    def test_update_task(self):
        # Test updating a task
        url = reverse('update_task', args=[2])
        data = {"title": "Updated Task", "completed": True}
        response = self.client.put(url, json.dumps(data), content_type='application/json')
        self.assertSuccess(response)

        # Test updating a non-existent task
        url = reverse('update_task', args=[10])
        response = self.client.put(url, json.dumps(data), content_type='application/json')
        self.assertError(response)

    def test_search_task(self):
        # Test searching for a task with a term in the title
        url = reverse('search_task', args=['test'])
        response = self.client.get(url)
        self.assertSuccess(response)
        data = json.loads(response.content)
        self.assertEqual(len(data['tasks']), 1)

        # Test searching for a non-existent task
        url = reverse('search_task', args=['random'])
        response = self.client.get(url)
        self.assertSuccess(response)
        data = json.loads(response.content)
        self.assertEqual(len(data['tasks']), 0)
