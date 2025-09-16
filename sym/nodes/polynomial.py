from __future__ import annotations

from .. import ArithmaticNode, Monomial


class Polynomial(ArithmaticNode):
    def __init__(self, *terms: Monomial, sort: bool = True):
        if sort:
            terms = tuple(
                sorted(
                    terms,
                    key=lambda term: max(var.exponent.value for var in term.variables),
                    reverse=True,
                )
            )
        self.terms = terms

    def to_latex_inline(self):
        if not self.terms:
            return ""

        latex = self.terms[0].to_latex_inline()

        for t in self.terms[1:]:
            if t.coefficient.value > 0:
                latex += " + " + t.to_latex_inline()
            else:
                latex += (
                    " - " + (-Monomial(t.coefficient, *t.variables)).to_latex_inline()
                )

        return latex
