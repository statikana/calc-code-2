from __future__ import annotations

from types import NotImplementedType
from typing import Any, overload, Self
from node import *

__all__ = ["Constant"]


class Constant(Node):
    """Single number."""

    def __init__(self, value: float):
        self.value = value

    @overload
    def __add__(self, other: Node) -> Add[Self, Node]: ...

    @overload
    def __add__(self, other: Self) -> Self: ...


    def __add__(self, other: object) -> Self | Add[Self, Node] | NotImplementedType:
        match other:
            case Constant():
                return Constant(self.value + other.value)
            case Node():
                return Add(self, other)
            case _:
                return NotImplemented

    def __sub__(self, other: NodeT) -> "Constant | Sub[Constant, NodeT]":
        match other:
            case Constant():
                return Constant(self.value - other.value)
            case _:
                return super().__sub__(other)

    def __mul__(self, other: NodeT) -> "Constant | Mul[Constant, NodeT]":
        match other:
            case Constant():
                return Constant(self.value * other.value)
            case _:
                return super().__mul__(other)

    def __truediv__(self, other: NodeT) -> "Constant | Div[Constant, NodeT]":
        match other:
            case Constant():
                return Constant(self.value / other.value)
            case _:
                return super().__truediv__(other)

    def __pow__(self, other: NodeT) -> "Constant | Pow[Constant, NodeT]":
        match other:
            case Constant():
                return Constant(self.value**other.value)
            case _:
                return super().__pow__(other)


C = Constant

