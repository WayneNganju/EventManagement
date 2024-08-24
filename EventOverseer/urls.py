from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrganizerViewSet, VenueViewSet, EventViewSet, ParticipantViewSet, TicketViewSet

router = DefaultRouter()
router.register(r'organizers', OrganizerViewSet)
router.register(r'venues', VenueViewSet)
router.register(r'events', EventViewSet)
router.register(r'participants', ParticipantViewSet)
router.register(r'tickets', TicketViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
