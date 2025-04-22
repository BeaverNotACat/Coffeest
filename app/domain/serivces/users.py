from typing import Any
from uuid import uuid4

from argon2 import PasswordHasher

from app.domain.exceptions.passwords import PasswordAlreadyInUseError
from app.domain.models.users import User
from app.domain.value_objects import UserID

password_hasher = PasswordHasher()
_sentinel: Any = object()


class UserService:
    @staticmethod
    def create_user(email: str, password: str = _sentinel) -> User:
        password_hash = None
        if password is not _sentinel:
            password_hash = password_hasher.hash(password)

        return User(
            id=UserID(uuid4()),
            email=email,
            password_hash=password_hash,
            tools=[],
        )

    @staticmethod
    def reset_password(user: User, new_password: str) -> User:
        if user.password_hash is not None and password_hasher.verify(
            user.password_hash, new_password
        ):
            raise PasswordAlreadyInUseError

        user.password_hash = password_hasher.hash(new_password)

        return user
