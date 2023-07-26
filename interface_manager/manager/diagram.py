from diagrams import Diagram
from diagrams.c4 import Person, Container, System, Relationship
from tempfile import NamedTemporaryFile
def create_diagram(filename, area="Ejemplo de Diagrama C4", interfaces={}, applications={}):

    with Diagram(area, filename=filename, show=False):
        for i in interfaces:
            origin = System(str(i.source), "Un cliente del banco")
            destination = System(str(i.destination), "destination system")
            origin >> Relationship(i.description) >> destination


if __name__ == "__main__":
    filename = NamedTemporaryFile(dir="./").name
    create_diagram(filename)
    with open(filename + ".png", "rb") as f:
        diagram_data = f.read()