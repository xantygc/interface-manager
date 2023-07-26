from diagrams import Diagram
from diagrams.c4 import Person, Container, System, Relationship
from tempfile import NamedTemporaryFile
def create_diagram(filename, area="Ejemplo de Diagrama C4", interfaces={}, applications={}):
    existing_elements = {}


    with Diagram(area, filename=filename, show=False):
        for i in interfaces:
            source_name = str(i.source)
            destination_name = str(i.destination)

            if source_name not in existing_elements:
                origin = System(source_name, "Un cliente del banco")
                existing_elements[source_name]=origin
            else:
                origin = existing_elements[source_name]

            if destination_name not in existing_elements:
                destination = System(destination_name, "Un cliente del banco")
                existing_elements[destination_name] = destination
            else:
                destination = existing_elements[destination_name]

            origin >> Relationship(i.description) >> destination


if __name__ == "__main__":
    filename = NamedTemporaryFile(dir="./").name

    create_diagram(filename)
    with open(filename + ".png", "rb") as f:
        diagram_data = f.read()