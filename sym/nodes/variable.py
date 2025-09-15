

class Variable(Node):
    def __init__(self, name: str, value: Constant | None = None):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"{self.name}={self.value or ''}"

    def latex_inline(self):
        return self.name
    

    def __add__(self, other: NodeT) -> Add[Self, NodeT]:
        return Add(self, other)

    def __sub__(self, other: NodeT) -> Sub[Self, NodeT]:
        return Sub(self, other)

    def __mul__(self, other: NodeT) -> Mul[Self, NodeT]:
        return Mul(self, other)

    def __truediv__(self, other: NodeT) -> Div[Self, NodeT]:
        return Div(self, other)

    def __pow__(self, other: NodeT) -> Pow[Self, NodeT]:
        return Pow(self, other)