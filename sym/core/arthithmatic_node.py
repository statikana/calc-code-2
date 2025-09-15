from typing import Self, TypeAlias
from .node import Node, NodeT
from .operator import Add, Sub, Mul, Div, Pow, Derivative, Integral, ExpressionT, RespectT, OrderT


__all__ = ["AriNode"]

class ArithmaticNode(Node):
    """"""
    def __add__(self, other: NodeT) -> Add[Self, NodeT]:
        return Add(self, other)

    def __sub__(self, other: NodeT) -> Sub[Self, NodeT]:
        return Sub(self, other)

    def __mul__(self, other: NodeT) -> Mul[Self, NodeT]:
        return Mul(self, other)

    def __truediv__(self, other: NodeT) -> Div[Self, NodeT]:
        return Div(self, other)

    def __pow__(self, other: NodeT) -> Pow[Self, NodeT]:
        return Pow(self, other)

    def derive(self, respect: RespectT, order: OrderT | None = None) -> Derivative[Self, RespectT, OrderT]:
        return Derivative(self, respect, order)
    
    def integrate(self, respect: RespectT, lower: Node | None = None, upper: Node | None = None) -> Integral[Self, RespectT]:
        return Integral(self, respect, lower, upper)
    
AriNode: TypeAlias = ArithmaticNode