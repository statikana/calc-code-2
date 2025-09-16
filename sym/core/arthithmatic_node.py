from typing import Self, Optional
from .node import Node
from .operator import Add, Sub, Mul, Div, Pow, Derivative, Integral


__all__ = ["ArithmaticNode"]


class ArithmaticNode(Node):
    """"""

    def __add__[OtherT: Node](self, other: OtherT) -> Add[Self, OtherT]:
        return Add(self, other)

    def __sub__[OtherT: Node](self, other: OtherT) -> Sub[Self, OtherT]:
        return Sub(self, other)

    def __mul__[OtherT: Node](self, other: OtherT) -> Mul[Self, OtherT]:
        return Mul(self, other)

    def __truediv__[OtherT: Node](self, other: OtherT) -> Div[Self, OtherT]:
        return Div(self, other)

    def __pow__[OtherT: Node](self, other: OtherT) -> Pow[Self, OtherT]:
        return Pow(self, other)

    def derive[RespectT: Node, OrderT: Node](
        self, respect: RespectT, order: Optional[OrderT] = None
    ) -> Derivative[Self, RespectT, OrderT]:
        return Derivative(self, respect, order)

    def integrate[RespectT: Node, LowerT: Node, UpperT: Node](
        self,
        respect: RespectT,
        lower: Optional[LowerT] = None,
        upper: Optional[UpperT] = None,
    ) -> Integral[Self, RespectT, LowerT, UpperT]:
        return Integral(self, respect, lower, upper)
