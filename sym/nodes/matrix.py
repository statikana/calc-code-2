from functools import cache
from .. import ArithmaticNode, Node


MatrixDimensionT = list[Node] | list["MatrixDimensionT"]

class Matrix(ArithmaticNode):
    def __init__(
        self,
        matrix: MatrixDimensionT
    ):
        self.matrix = matrix
    
    @property  # does not ensure size safety, only checks first element of each dimension
    @cache
    def shape(self) -> tuple[int, ...]:
        shape = []

        interest = self.matrix
        max_dimensions = 10000

        while len(shape) < max_dimensions:
            if isinstance(interest, list):
                shape.append(len(interest))
                interest = interest[0]
            else:
                break
        
        return tuple(shape)
    
    def to_latex_inline(self):
        shape = self.shape
        if len(shape) == 0:
            return ""
        start = "\\begin{{bmatrix}}"
        end = "\\end{{bmatrix}}"
        if len(shape) == 1:
            array: tuple[Node] = self.matrix  # type: ignore
            middle = f"{' & '.join(item.to_latex_inline() for item in array)}"
        elif len(shape) == 2:
            middle = "\\\\\n".join(
                f"{' & '.join(item.to_latex_inline() for item in array)}"  # type: ignore
                for array in self.matrix
            )
        else:
            return NotImplemented
        return f"{start}\n{middle}\n{end}"