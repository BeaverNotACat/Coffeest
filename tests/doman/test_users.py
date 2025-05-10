import pytest

from app.domain.exceptions.passwords import PasswordAlreadyInUseError
from app.domain.models.brewing_tools import BrewingTool
from app.domain.models.users import User
from app.domain.services.users import UserService


def test_create_user_with_password(
    user_service: UserService, user_email: str, user_password: str
) -> None:
    user = user_service.create_user(user_email, user_password)

    assert user.email == user_email
    assert user.password_hash is not None
    assert user.tools == []


def test_create_user_without_password(
    user_service: UserService, user_email: str
) -> None:
    user = user_service.create_user(user_email)

    assert user.email == user_email
    assert user.password_hash is None
    assert user.tools == []


def test_password_reset(user_service: UserService, mock_user: User) -> None:
    new_password = 'new_password'
    old_hash = mock_user.password_hash

    user_service.reset_password(mock_user, new_password)

    assert mock_user.password_hash != old_hash


def test_password_reset_cant_be_same(
    user_service: UserService, mock_user: User, user_password: str
) -> None:
    with pytest.raises(PasswordAlreadyInUseError):
        user_service.reset_password(mock_user, user_password)


def test_user_add_tool(
    mock_user: User, mock_brewing_tool: BrewingTool
) -> None:
    mock_user.add_tool(mock_brewing_tool)

    assert mock_user.tools.pop() == mock_brewing_tool


def test_user_remove_tool(
    mock_user: User, mock_brewing_tool: BrewingTool
) -> None:
    mock_user.add_tool(mock_brewing_tool)
    mock_user.remove_tool(mock_brewing_tool)

    assert mock_brewing_tool not in mock_user.tools


def test_user_cant_add_same_tools(
    mock_user: User, mock_brewing_tool: BrewingTool
) -> None:
    mock_user.add_tool(mock_brewing_tool)
    tools_count = len(mock_user.tools)

    mock_user.add_tool(mock_brewing_tool)

    assert mock_user.tools.count(mock_brewing_tool) == tools_count


def test_user_cant_remove_unexisting_tools(
    mock_user: User, mock_brewing_tool: BrewingTool
) -> None:
    mock_user.remove_tool(mock_brewing_tool)
    tools_count = len(mock_user.tools)

    mock_user.remove_tool(mock_brewing_tool)

    assert mock_user.tools.count(mock_brewing_tool) == tools_count
