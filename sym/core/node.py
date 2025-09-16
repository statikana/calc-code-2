from __future__ import annotations
from typing import TypeVar

__all__ = ["Node"]


class Node:
    """Basic class which all other object classes inherit from."""

    def latex(
        self,
    ) -> str:
        return f"\\[\n{self.latex_inline()}\n\\]"

    def latex_inline(self) -> str:
        return NotImplemented
