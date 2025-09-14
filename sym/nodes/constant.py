from __future__ import annotations
from ..core.core import Node

class Constant(Node):
    def __init__(self, value: float):
        self.value = value

    def __repr__(self):
        return str(self.value)

    def latex_inline(self):
        return str(self.value)


class Variable(Node):
    def __init__(self, name: str, value: Constant | None = None):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"{self.name}={self.value or ''}"

    def latex_inline(self):
        return self.name
