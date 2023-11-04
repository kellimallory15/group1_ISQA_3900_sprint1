from django.urls import path
from . import views

urlpatterns = [
    # Path Converters
    # int: numbers
    # str: strings
    # path: whole urls /
    # slug: hyphen-and_underscores_stuff
    # UUID: universally unique identifier

    path('', views.home, name="home"),
    path('<int:year>/<str:month>/', views.home, name="home"),
    path('bookings', views.all_events, name="list-events"),
    path('add_package', views.add_venue, name='add-venue'),
    path('list_packages', views.list_venues, name='list-venues'),
    path('show_package/<venue_id>', views.show_venue, name='show-venue'),
    path('search_packages', views.search_venues, name='search-venues'),
    path('update_package/<venue_id>', views.update_venue, name='update-venue'),
    path('update_booking/<event_id>', views.update_event, name='update-event'),
    path('add_booking', views.add_event, name='add-event'),
    path('delete_booking/<event_id>', views.delete_event, name='delete-event'),
    path('delete_package/<venue_id>', views.delete_venue, name='delete-venue'),
    path('package_text', views.venue_text, name='venue_text'),
    path('package_csv', views.venue_csv, name='venue_csv'),
    path('package_pdf', views.venue_pdf, name='venue_pdf'),
    path('my_bookings', views.my_events, name='my_events'),
    path('search_bookings', views.search_events, name='search_events'),
    path('admin_approval', views.admin_approval, name='admin_approval'),
    path('package_bookings/<venue_id>', views.venue_events, name='venue-events'),
    path('show_booking/<event_id>', views.show_event, name='show-event'),
]
