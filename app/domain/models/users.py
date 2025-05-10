from typing import TYPE_CHECKING, Annotated

from msgspec import Meta, Struct

from app.domain.value_objects import UserID

if TYPE_CHECKING:  # pragma: no cover
    from .brewing_tools import BrewingTool


class User(Struct):
    id: UserID
    email: Annotated[
        str, Meta(pattern='[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[A-Z]{2,}')
    ]
    password_hash: str | None
    tools: list['BrewingTool']

    def add_tool(self, tool: 'BrewingTool') -> None:
        if tool in self.tools:
            return
        self.tools.append(tool)

    def remove_tool(self, tool: 'BrewingTool') -> None:
        if tool not in self.tools:
            return
        tool_index = self.tools.index(tool)
        del self.tools[tool_index]
