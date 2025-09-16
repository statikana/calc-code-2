from .. import ArithmaticNode, Constant


__all__ = ["Variable"]


class Variable(ArithmaticNode):
    def __init__(self, name: str, value: Constant | None = None):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"{self.name}={self.value or ''}"

    def to_latex_inline(self):
        return self.name
