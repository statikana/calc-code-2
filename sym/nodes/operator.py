from __future__ import annotations
from typing import Generic, TypeVar
from .. import *


NodeT = TypeVar("NodeT", bound=Node)
LHSNodeT = TypeVar("LHSNodeT", bound=Node)
RHSNodeT = TypeVar("RHSNodeT", bound=Node)


class Operator(Node):
    """Represents an unresolved operation between two nodes."""


class Add(Generic[LHSNodeT, RHSNodeT]):
    def __init__(self, lhs: LHSNodeT, rhs: RHSNodeT):
        self.lhs = lhs
        self.rhs = rhs

    def __repr__(self):
        return f"{self.lhs} + {self.rhs}"

    def latex_inline(self):
        return f"{self.lhs.latex_inline()} + {self.rhs.latex_inline()}"


class Sub(Generic[LHSNodeT, RHSNodeT]):
    def __init__(self, lhs: LHSNodeT, rhs: RHSNodeT):
        self.lhs = lhs
        self.rhs = rhs

    def __repr__(self):
        return f"{self.lhs} - {self.rhs}"

    def latex_inline(self):
        return f"{self.lhs.latex_inline()} - {self.rhs.latex_inline()}"


class Mul(Generic[LHSNodeT, RHSNodeT]):
    def __init__(self, lhs: LHSNodeT, rhs: RHSNodeT):
        self.lhs = lhs
        self.rhs = rhs

    def __repr__(self):
        return f"{self.lhs} * {self.rhs}"

    def latex_inline(self):
        return f"{self.lhs.latex_inline()} * {self.rhs.latex_inline()}"


class Div(Generic[LHSNodeT, RHSNodeT]):
    def __init__(self, lhs: LHSNodeT, rhs: RHSNodeT):
        self.lhs = lhs
        self.rhs = rhs

    def __repr__(self):
        return f"{self.lhs} / {self.rhs}"

    def latex_inline(self):
        return f"\\frac{{{self.lhs.latex_inline()}}}{{{self.rhs.latex_inline()}}}"


class Pow(Generic[LHSNodeT, RHSNodeT]):
    def __init__(self, lhs: LHSNodeT, rhs: RHSNodeT):
        self.lhs = lhs
        self.rhs = rhs

    def __repr__(self):
        return f"{self.lhs} ^ {self.rhs}"

    def latex_inline(self):
        return f"{self.lhs.latex_inline()}^{{{self.rhs.latex_inline()}}}"


ExpressionT = TypeVar("ExpressionT", bound=Node)
RespectT = TypeVar("RespectT", bound=Node)


class Derivative(Operator, Generic[ExpressionT, RespectT]):
    def __init__(
        self, expr: ExpressionT, respect: RespectT, order: Constant | None = None
    ):
        self.expr = expr
        self.respect = respect
        self.order = order or Constant(1)

    def latex_inline(self):
        expr_latex = self.expr.latex_inline()
        respect_latex = self.respect.latex_inline()
        is_short = isinstance(self.expr, (Variable, Constant))

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


class Integral(Operator, Generic[ExpressionT, RespectT]):
    def __init__(
        self,
        expr: ExpressionT,
        respect: RespectT,
        lower: Node | None = None,
        upper: Node | None = None,
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
