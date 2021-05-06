TITLE       = ""
DESCRIPTION = """
"""

from raytracing import *

def exempleCode(comments=None):
    path = ImagingPath()
    path.label = TITLE
    path.append(Space(d=4))
    path.append(Lens(f=4, diameter=0.8, label='Obj'))
    path.append(Space(d=4 + 180))
    path.append(Lens(f=180, diameter=5.0, label='Tube Lens'))
    path.append(Space(d=180))
    path.display(comments=comments)

if __name__ == "__main__":
    exempleCode()