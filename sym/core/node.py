from __future__ import annotations
from abc import abstractmethod
from typing import TypeVar

__all__ = ["Node", "NodeT"]


class Node:
    """Basic class which all other object classes inherit from."""

    def latex(
        self,
    ) -> str:
        return f"\\[\n{self.to_latex_inline()}\n\\]"

    @abstractmethod
    def to_latex_inline(self) -> str:
        return NotImplemented

    def __init_subclass__(cls, level: int):
        cls.level = level
        super().__init_subclass__()


NodeT = TypeVar("NodeT", bound=Node)