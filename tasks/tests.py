from django.test import TestCase, Client
from django.urls import reverse
from .models import Task


class TaskModelTest(TestCase):
    """Test cases for Task model"""
    
    def setUp(self):
        self.task = Task.objects.create(
            title="Test Task",
            description="Test Description"
        )
    
    def test_task_creation(self):
        self.assertEqual(self.task.title, "Test Task")
        self.assertEqual(self.task.status, "pending")
        self.assertFalse(self.task.is_completed())
    
    def test_task_completion(self):
        self.task.status = "completed"
        self.task.save()
        self.assertTrue(self.task.is_completed())


class TaskViewTest(TestCase):
    """Test cases for Task views"""
    
    def setUp(self):
        self.client = Client()
        self.task = Task.objects.create(
            title="Test Task",
            description="Test Description"
        )
    
    def test_task_list_view(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")
    
    def test_task_detail_view(self):
        response = self.client.get(reverse('task_detail', args=[self.task.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")
    
    def test_task_create_view_get(self):
        response = self.client.get(reverse('task_create'))
        self.assertEqual(response.status_code, 200)
    
    def test_task_create_view_post(self):
        data = {
            'title': 'New Task',
            'description': 'New Description',
            'status': 'pending'
        }
        response = self.client.post(reverse('task_create'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(title='New Task').exists())
