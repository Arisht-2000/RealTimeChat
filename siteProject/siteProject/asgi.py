"""
ASGI config for siteProject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'siteProject.settings')

djangoASGI_app = get_asgi_application()

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    "http": djangoASGI_app,
    # Just HTTP for now. (We can add other protocols later.)
    
    # "websocket": get_asgi_application(),
    # "websocket": AuthMiddlewareStack(
    #     URLRouter(
    #         websocket_urlpatterns
    #     )
    # ),
})