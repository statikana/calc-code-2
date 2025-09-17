from .. import ArithmaticNode


__all__ = ["Integer"]


class Integer(ArithmaticNode, level=3):
    def __init__(self, value: int):
        self.value = value

    def __neg__(self):
        return Integer(-self.value)

    def to_latex_inline(self):
        return str(self.value)
