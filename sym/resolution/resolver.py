from abc import abstractmethod
from typing import Protocol, TypeVar, TypeVarTuple
from .. import (
    Node,
    ArithmaticNode,
    Operator,
    Constant,
    Variable,
    Integer,
    Monomial,
    Polynomial,
    Matrix,
    Add,
    Sub,
    Mul,
    Div,
    Pow,
    Derivative,
    Product,
)

OperatorT = TypeVar("OperatorT", bound=Operator, contravariant=True)
NodeT = TypeVar("NodeT", bound=Node)

class Resolver(Protocol[OperatorT, *NodeT]):
    """Represents a class which contains a .evaluate method which can resolve an operation between Node1 and Node2"""

    @abstractmethod
    def evaluate(
        self,
        op: OperatorT,
        nodes: NodeTs
    ) -> Node:
        return NotImplemented


class DivCC(Resolver[Div, (Constant, Constant)]):
    def evaluate(self, op: Div, nodes: tuple[Constant, Constant]) -> Node:
        return super().evaluate(op, nodes)