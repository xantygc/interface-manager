from diagrams import Diagram
from diagrams.c4 import Person, Container, System, Relationship
from tempfile import NamedTemporaryFile
def create_diagram(filename, area="Ejemplo de Diagrama C4"):
    with Diagram(area, filename=filename, show=False):
        customer = Person("Cliente", "Un cliente del banco")
        webapp = Container("Aplicación Web", "Java/Spring")
        database = Container("Base de Datos", "Oracle")

        customer >> Relationship("Utiliza") >> webapp >> Relationship("Utiliza") >> database



if __name__ == "__main__":
    filename = NamedTemporaryFile(dir="./").name
    create_diagram(filename)
    with open(filename + ".png", "rb") as f:
        diagram_data = f.read()