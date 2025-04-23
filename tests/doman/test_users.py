from uuid import uuid4

import pytest

from app.adapters.password import PasswordHasher
from app.domain.exceptions.passwords import PasswordAlreadyInUseError
from app.domain.models.brewing_tools import BrewingTool
from app.domain.models.users import User
from app.domain.services.users import UserService
from app.domain.value_objects import BrewingToolID, UserID


@pytest.fixture
def password_hasher() -> PasswordHasher:
    return PasswordHasher()


@pytest.fixture
def password() -> str:
    return 'some_password'


@pytest.fixture
def new_password() -> str:
    return 'new_password'


@pytest.fixture
def mock_user(password_hasher, password) -> User:
    return User(
        id=UserID(uuid4()),
        email='some@example.com',
        password_hash=password_hasher.hash(password),
        tools=[],
    )


@pytest.fixture
def mock_tool() -> BrewingTool:
    return BrewingTool(
        id=BrewingToolID(uuid4()),
        name='tool_name',
        method=None,
        is_global=False,
    )


def test_create_user_with_password(password_hasher, password):
    email = 'some@example.com'
    service = UserService(password_hasher)

    user = service.create_user(email, password)

    assert user.email == email
    assert user.password_hash is not None
    assert user.tools == []


def test_create_user_without_password(password_hasher):
    email = 'some@example.com'
    service = UserService(password_hasher)

    user = service.create_user(email)

    assert user.email == email
    assert user.password_hash is None
    assert user.tools == []


def test_password_reset(password_hasher, mock_user, new_password):
    service = UserService(password_hasher)
    old_password = mock_user.password_hash

    service.reset_password(mock_user, new_password)

    assert mock_user.password_hash != old_password


def test_password_reset_cant_be_same(password_hasher, mock_user, password):
    service = UserService(password_hasher)

    with pytest.raises(PasswordAlreadyInUseError):
        service.reset_password(mock_user, password)


def test_user_add_tool(mock_user, mock_tool):
    mock_user.add_tool(mock_tool)

    assert mock_user.tools.pop() == mock_tool


def test_user_cant_add_same_tools(mock_user, mock_tool):
    tools_count = len(mock_user.tools) + 1

    mock_user.add_tool(mock_tool)
    mock_user.add_tool(mock_tool)

    assert len(mock_user.tools) == tools_count
