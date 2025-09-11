from node import *
from ..constant import Constant

class Variable(Node):
    def __init__(self, name: str, value: Constant | None = None):
        self.name=name
        self.value = value