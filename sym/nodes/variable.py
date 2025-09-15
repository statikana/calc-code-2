from typing import Self
from .. import *


__all__ = ["Variable"]


class Variable(AriNode):
    def __init__(self, name: str, value: Constant | None = None):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"{self.name}={self.value or ''}"

    def latex_inline(self):
        return self.name