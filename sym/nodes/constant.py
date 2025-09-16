from .. import *


__all__ = ["Constant"]


class Constant(ArithmaticNode):
    def __init__(self, value: float):
        self.value = value

    def __repr__(self):
        return str(self.value)

    def latex_inline(self):
        return str(self.value)
