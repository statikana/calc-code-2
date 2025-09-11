from typing import Generic, Self, TypeVar


class Node:
    """Basic class which all other object classes inherit from."""


NodeT = TypeVar("NodeT", bound=Node)
LHSNodeT = TypeVar("LHSNodeT", bound=Node)
RHSNodeT = TypeVar("RHSNodeT", bound=Node)

    
class Operator(Node):
    """Represents an unresolved operation between two nodes."""
    pass

class _BinSidedOperator(Operator, Generic[LHSNodeT, RHSNodeT]):
    def __init__(self, lhs: LHSNodeT, rhs: RHSNodeT):
        self.lhs = lhs
        self.rhs = rhs


class Add(_BinSidedOperator, Generic[LHSNodeT, RHSNodeT]): pass
class Sub(_BinSidedOperator, Generic[LHSNodeT, RHSNodeT]): pass
class Mul(_BinSidedOperator, Generic[LHSNodeT, RHSNodeT]): pass
class Div(_BinSidedOperator, Generic[LHSNodeT, RHSNodeT]): pass
class Pow(_BinSidedOperator, Generic[LHSNodeT, RHSNodeT]): pass