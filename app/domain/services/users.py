from typing import Annotated, Any
from uuid import uuid4

from annotated_types import MinLen

from app.adapters.password import PasswordHasher
from app.domain.exceptions.passwords import PasswordAlreadyInUseError
from app.domain.models.users import User
from app.domain.value_objects import UserID

_sentinel: Any = object()


class UserService:
    def __init__(self, password_hasher: PasswordHasher):
        self.password_hasher = password_hasher

    def create_user(
        self, email: str, password: Annotated[str, MinLen(8)] = _sentinel
    ) -> User:
        """
        Creates user
        Supports email passwords auth and OAuth with only email
        """
        password_hash = None
        if password is not _sentinel:
            password_hash = self.password_hasher.hash(password)

        return User(
            id=UserID(uuid4()),
            email=email,
            password_hash=password_hash,
            tools=[],
        )

    def reset_password(self, user: User, new_password: str) -> User:
        """
        Sets new password hash

        Password resetting is a service method
        cause of PasswordHasher dependencie
        """
        if user.password_hash is not None and self.password_hasher.verify(
            user.password_hash, new_password
        ):
            raise PasswordAlreadyInUseError
        user.password_hash = self.password_hasher.hash(new_password)
        return user
