from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Organizer, Venue, Event

class EventOverseerTests(APITestCase):

    def test_create_organizer(self):
        url = reverse('organizer-list')
        data = {'name': 'Jane Smith', 'email': 'jane.smith@example.com', 'phone_number': '0987654321'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_venue(self):
        url = reverse('venue-list')
        data = {'name': 'Crystal Ballroom', 'location': '456 Elm St', 'capacity': 300}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_event(self):
        organizer = Organizer.objects.create(name='Jane Smith', email='jane.smith@example.com', phone_number='0987654321')
        venue = Venue.objects.create(name='Crystal Ballroom', location='456 Elm St', capacity=300)
        url = reverse('event-list')
        data = {
            'name': 'Innovation Summit', 
            'description': 'A summit focused on innovation.', 
            'start_date': '2024-09-15T09:00:00Z', 
            'end_date': '2024-09-15T17:00:00Z', 
            'venue': venue.id, 
            'organizer': organizer.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
