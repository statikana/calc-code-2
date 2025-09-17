from .. import ArithmaticNode


__all__ = ["Constant"]


class Constant(ArithmaticNode, level=3):
    def __init__(self, value: float):
        self.value = value

    def __neg__(self):
        return Constant(-self.value)

    def to_latex_inline(self):
        return str(self.value)
