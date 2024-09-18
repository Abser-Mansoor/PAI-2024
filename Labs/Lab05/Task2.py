import abc
from abc import *

class shape(ABC) :
    def __init__(self, dimensions) :
        self.dimensions = dimensions
    @abstractmethod
    def area(self) :
        pass

class rectangle(shape) :
    def __init__(self,dimensions) :
        super().__init__(dimensions)
    def area(self, length, breadth) :
        return length*breadth
    
class triangle(shape) :
    def __init__(self,dimensions) :
        super().__init__(dimensions)
    def area(self, base, height) :
        return base*height*0.5
    
class square(shape) :
    def __init__(self,dimensions) :
        super().__init__(dimensions)
    def area(self, length) :
        return length*length


rect = rectangle(4)
tri = triangle(3)
squ = square(4)
print(f"Rectangle has area {rect.area(5,9)}\nTriangle has area {tri.area(3,5)}\nSquare has area {squ.area(3)}")
