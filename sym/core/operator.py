from __future__ import annotations
from typing import Generic, Optional, TypeVar, TypeVarTuple
from .node import Node

NodeT = TypeVar("NodeT", bound=Node)
LHSNodeT = TypeVar("LHSNodeT", bound=Node)
RHSNodeT = TypeVar("RHSNodeT", bound=Node)


__all__ = [
    "Operator",
    "Add",
    "Sub",
    "Mul",
    "Div",
    "Pow",
    "Derivative",
    "Integral",
    "Product",
]


class Operator(Node):
    """Represents an unresolved operation between two nodes."""


class Add[LHSNodeT: Node, RHSNodeT: Node](Operator):
    def __init__(self, lhs: LHSNodeT, rhs: RHSNodeT):
        self.lhs = lhs
        self.rhs = rhs

    def __repr__(self):
        return f"{self.lhs} + {self.rhs}"

    def latex_inline(self):
        return f"{self.lhs.latex_inline()} + {self.rhs.latex_inline()}"


class Sub[LHSNodeT: Node, RHSNodeT: Node](Operator):
    def __init__(self, lhs: LHSNodeT, rhs: RHSNodeT):
        self.lhs = lhs
        self.rhs = rhs

    def __repr__(self):
        return f"{self.lhs} - {self.rhs}"

    def latex_inline(self):
        return f"{self.lhs.latex_inline()} - {self.rhs.latex_inline()}"
    
class Mul[LHSNodeT: Node, RHSNodeT: Node](Operator):
    def __init__(self, lhs: LHSNodeT, rhs: RHSNodeT):
        self.lhs = lhs
        self.rhs = rhs

    def __repr__(self):
        return f"{self.lhs} * {self.rhs}"

    def latex_inline(self):
        return f"{self.lhs.latex_inline()} * {self.rhs.latex_inline()}"

# class Product[*FactorT: [Node, ...]](Operator):
#     def __init__(self, factors: tuple[*FactorT]):
#         self.factors = factors 

#     def __repr__(self):
#         return " * ".join(map(str, self.factors))

#     def latex_inline(self):
#         return " * ".join(map(lambda f: f.latex_inline(), self.factors))


class Div[LHSNodeT: Node, RHSNodeT: Node]:
    def __init__(self, lhs: LHSNodeT, rhs: RHSNodeT):
        self.lhs = lhs
        self.rhs = rhs

    def __repr__(self):
        return f"{self.lhs} / {self.rhs}"

    def latex_inline(self):
        return f"\\frac{{{self.lhs.latex_inline()}}}{{{self.rhs.latex_inline()}}}"


class Pow[LHSNodeT: Node, RHSNodeT: Node]:
    def __init__(self, lhs: LHSNodeT, rhs: RHSNodeT):
        self.lhs = lhs
        self.rhs = rhs

    def __repr__(self):
        return f"{self.lhs} ^ {self.rhs}"

    def latex_inline(self):
        return f"{self.lhs.latex_inline()}^{{{self.rhs.latex_inline()}}}"


class Derivative[ExpressionT: Node, RespectT: Node, OrderT: Node](Operator):
    def __init__(
        self, expr: ExpressionT, respect: RespectT, order: OrderT | None = None
    ):
        self.expr = expr
        self.respect = respect
        self.order = order

    def latex_inline(self):
        expr_latex = self.expr.latex_inline()
        respect_latex = self.respect.latex_inline()
        is_short = len(expr_latex) == 1

        if self.order == 1:
            return (
                f"\\frac{{d {expr_latex}}}{{d {respect_latex}}}"
                if is_short
                else f"\\frac{{d}}{{d {respect_latex}}}{expr_latex}"
            )
        else:
            return (
                f"\\frac{{d^{{{self.order}}} {expr_latex}}}{{d {respect_latex}^{{{self.order}}}}}"
                if is_short
                else f"\\frac{{d^{{{self.order}}}}}{{d {respect_latex}^{{{self.order}}}}}{expr_latex}"
            )


class Integral[ExpressionT: Node, RespectT: Node, LowerT: Node, UpperT: Node](Operator):
    def __init__(
        self,
        expr: ExpressionT,
        respect: RespectT,
        lower: Optional[LowerT] = None,
        upper: Optional[UpperT] = None,
    ):
        self.expr = expr
        self.respect = respect
        self.lower = lower
        self.upper = upper

    def latex_inline(self):
        expr_latex = self.expr.latex_inline()
        respect_latex = self.respect.latex_inline()

        if self.lower is not None and self.upper is not None:
            lower_latex = self.lower.latex_inline()
            upper_latex = self.upper.latex_inline()
            return f"\\int_{{{lower_latex}}}^{{{upper_latex}}} {expr_latex} \\, d{respect_latex}"
        else:
            return f"\\int {expr_latex} \\, d{respect_latex}"
