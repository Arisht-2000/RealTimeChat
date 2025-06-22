"""
ASGI config for siteProject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'siteProject.settings')

djangoASGI_app = get_asgi_application()

from chatApp.routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    "http": djangoASGI_app,
    "websocket" : AllowedHostsOriginValidator(
        AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
    )
})