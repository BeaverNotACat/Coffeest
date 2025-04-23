from dishka import make_container

from .user_service import UserServiceProvider

container = make_container(UserServiceProvider())
