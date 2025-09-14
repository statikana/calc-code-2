from __future__ import annotations
from typing import TypeVar

__all__ = ["Node", "NodeT"]


class Node:
    """Basic class which all other object classes inherit from."""

    def latex(
        self,
    ) -> (
        str
    ):  # only defined for Node parent class, calls to children are brought to this method, which uses the child's latex method
        return f"\\[\n{self.latex_inline()}\n\\]"

    def latex_inline(self) -> str:
        return NotImplemented

    def simplify(self) -> Node:
        return NotImplemented  # TODO

    def derive(self, respect: ..., order: ...) -> ...:
        return NotImplemented


NodeT = TypeVar("NodeT", bound=Node)
