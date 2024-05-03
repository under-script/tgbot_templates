"""Import all routers and add them to routers_list."""
from .admin import admin_router
from .contact import contact_router
from .echo import echo_router
from .location import location_router
from .send_photos import media_router
from .user import user_router

routers_list = [
    # admin_router,
    user_router,
    contact_router,
    location_router,
    media_router,
    # echo_router,  # echo_router must be last
]

__all__ = [
    "routers_list",
]
