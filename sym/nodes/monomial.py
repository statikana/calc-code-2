from .. import ArithmaticNode, Constant, Pow, Variable, Integer


class Monomial(ArithmaticNode, level=4):
    def __init__(self, coefficient: Constant, *variables: Pow[Variable, Integer]):
        self.coefficient = coefficient
        self.variables = sorted(
            variables, key=lambda p: p.base.name, reverse=False
        )  # sorted by variable names

    def __neg__(self):
        return Monomial(-self.coefficient, *self.variables)

    def to_latex_inline(self):
        return f"{self.coefficient.value}" + "".join(
            (
                f"{{{p.base.name}}}^{{{p.exponent.value}}}"
                if p.exponent.value != 1
                else p.base.name
            )
            for p in self.variables
        )
