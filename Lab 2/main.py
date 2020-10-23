from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import numpy as np

def main():
    r = Rectangle("синего", 7, 4)
    c = Circle("зелёного", 9)
    s = Square("красного", 2)
    print(r)
    print(c)
    print(s)

    a = np.array([r.square(), c.square(), s.square()], float)
    for f in a:
        print(f)

if __name__ == "__main__":
    main()
