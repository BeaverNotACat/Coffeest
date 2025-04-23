from argon2 import PasswordHasher as Argon2Hasher
from argon2.exceptions import VerificationError


class PasswordHasher:
    def __init__(self) -> None:
        self.ph = Argon2Hasher()  # TODO: Add settings

    def hash(self, password: str) -> str:
        return self.ph.hash(password)

    def verify(self, password_hash: str, password: str) -> bool:
        try:
            is_verified: bool = self.ph.verify(password_hash, password)
        except VerificationError:
            is_verified = False
        return is_verified
