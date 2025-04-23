from dishka import Provider, Scope, provide

from app.adapters.password import PasswordHasher
from app.domain.services.users import UserService


class UserServiceProvider(Provider):
    scope = Scope.APP

    @provide
    def provide_password_hasher(self) -> PasswordHasher:
        return PasswordHasher()

    @provide
    def provide_user_service(
        self, password_hasher: PasswordHasher
    ) -> UserService:
        return UserService(password_hasher)
