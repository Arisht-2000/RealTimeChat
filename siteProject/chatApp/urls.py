from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),    # Home page
    #path('chat/<str:room_name>/', views.room, name='room'),  # Chat room page
    #path('create_room/', views.create_room, name='create_room'),  # Create a new chat room
    #path('join_room/', views.join_room, name='join_room'),  # Join an existing chat room
    #path('leave_room/<str:room_name>/', views.leave_room, name='leave_room'),  # Leave a chat room
    #path('send_message/', views.send_message, name='send_message'),  # Send a message in a chat room
    #path('get_messages/<str:room_name>/', views.get_messages, name='get_messages'),  # Get messages from a chat room
    #path('get_rooms/', views.get_rooms, name='get_rooms'),  # Get list of chat rooms
    #path('delete_room/<str:room_name>/', views.delete_room, name='delete_room'),  # Delete a chat room
    #path('edit_room/<str:room_name>/', views.edit_room, name='edit_room'),  # Edit a chat room
    #path('search_rooms/', views.search_rooms, name='search_rooms'),  # Search for chat rooms
    #path('user_profile/<str:username>/', views.user_profile, name='user_profile'),  # User profile page
    #path('edit_profile/', views.edit_profile, name='edit_profile'),  # Edit user profile
    #path('delete_account/', views.delete_account, name='delete_account'),  # Delete user account
    #path('notifications/', views.notifications, name='notifications'),  # User notifications
    #path('mark_notification_read/<int:notification_id>/', views.mark_notification_read, name='mark_notification_read'),  # Mark notification as read
    #path('delete_notification/<int:notification_id>/', views.delete_notification, name='delete_notification'),  # Delete a notification
    #path('report_user/<str:username>/', views.report_user, name='report_user'),  # Report a user
    #path('block_user/<str:username>/', views.block_user, name='block_user'),  # Block a user
    #path('unblock_user/<str:username>/', views.unblock_user, name='unblock_user'),  # Unblock a user
    #path('blocked_users/', views.blocked_users, name='blocked_users'),  # List of blocked users
    #path('user_settings/', views.user_settings, name='user_settings'),  # User settings page
    #path('change_password/', views.change_password, name='change_password'),  # Change user password
    #path('reset_password/', views.reset_password, name='reset_password'),  # Reset user password
    #path('privacy_policy/', views.privacy_policy, name='privacy_policy'),  # Privacy policy page
    #path('terms_of_service/', views.terms_of_service, name='terms_of_service'),  # Terms of service page
    #path('help/', views.help, name='help'),  # Help page
    #path('contact_support/', views.contact_support, name='contact_support'),  # Contact support page
    #path('faq/', views.faq, name='faq'),  # Frequently Asked Questions page
    #path('about/', views.about, name='about'),  # About the application page
    #path('feedback/', views.feedback, name='feedback'),  # User feedback page
    #path('report_bug/', views.report_bug, name='report_bug'),  # Report a bug page
    #path('feature_request/', views.feature_request, name='feature_request'),  # Feature request
    #path('logout/', views.logout_view, name='logout'),  # Logout user
    #path('login/', views.login_view, name='login'),  # Login page
    #path('register/', views.register, name='register'),  # User registration page
    #path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),  # Account activation
    #path('resend_activation/', views.resend_activation, name='resend_activation'),  # Resend activation email
]