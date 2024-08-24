
---

# Event Management System - Group5

## Overview

This repository contains the code for a Django API project for an Event Management System with an app called EventOverseer, developed by us Group 5 as part of the mini project for BBT3101: Application Programming for The Internet.

## Group Members

- Wayne Nganju - 146832
- Daniel Kaguai - 152439
- Tryon Otieno - 151115

## Project Details

### Models

The Event Management System includes the following models:

1. **Event**
   - `id` (Integer, Primary Key)
   - `name` (CharField, 100 characters)
   - `date` (DateTimeField)
   - `location` (CharField, 255 characters)
   - `description` (TextField)

2. **Organizer**
   - `id` (Integer, Primary Key)
   - `name` (CharField, 100 characters)
   - `contact` (CharField, 50 characters)

3. **Attendee**
   - `id` (Integer, Primary Key)
   - `name` (CharField, 100 characters)
   - `email` (EmailField)
   - `phone_number` (CharField, 15 characters)

4. **Ticket**
   - `id` (Integer, Primary Key)
   - `event` (ForeignKey to Event)
   - `attendee` (ForeignKey to Attendee)
   - `purchase_date` (DateTimeField)

5. **Venue**
   - `id` (Integer, Primary Key)
   - `name` (CharField, 100 characters)
   - `address` (CharField, 255 characters)
   - `capacity` (Integer)

### Serializers

Serializers are created to handle data transformation between JSON and Python objects. The following serializers are used:

1. **EventSerializer** - Serializes Event data.
2. **OrganizerSerializer** - Serializes Organizer data.
3. **AttendeeSerializer** - Serializes Attendee data.
4. **TicketSerializer** - Serializes Ticket data.
5. **VenueSerializer** - Serializes Venue data.

Validation rules are implemented in the serializers to ensure data integrity.

### Views/Viewsets

The API endpoints for CRUD operations are handled by the following viewsets:

1. **EventViewSet** - Handles CRUD operations for Event.
2. **OrganizerViewSet** - Handles CRUD operations for Organizer.
3. **AttendeeViewSet** - Handles CRUD operations for Attendee.
4. **TicketViewSet** - Handles CRUD operations for Ticket.
5. **VenueViewSet** - Handles CRUD operations for Venue.

### URLs

The URL patterns are defined to route HTTP requests to the appropriate viewsets:

- `/api/events/` - Routes to EventViewSet.
- `/api/organizers/` - Routes to OrganizerViewSet.
- `/api/attendees/` - Routes to AttendeeViewSet.
- `/api/tickets/` - Routes to TicketViewSet.
- `/api/venues/` - Routes to VenueViewSet.

### Testing

Unit tests for all API endpoints are included, covering all HTTP methods (GET, POST, PUT, DELETE). Tests can be run using Django’s built-in test framework or Postman.

### Setup

To set up the project locally, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/WayneNganju/EventManagementSystem-Group5]
   ```

2. **Navigate to the Project Directory**
   ```bash
   cd EventManagementSystem-Group5
   ```

3. **Create and Activate a Virtual Environment**
   ```bash
   python -m .venv venv
   source .venv\Scripts\activate
   ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser (Optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

8. **Access the API**
   Open your browser and navigate to `http://localhost:8000/api/`.

### Documentation

The documentation for the API endpoints, models, and their relationships is available in this README file. 

### Testing

All API endpoints have been tested using Django’s built-in test framework.
