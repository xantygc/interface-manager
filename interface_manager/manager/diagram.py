from tempfile import NamedTemporaryFile

from diagrams import Diagram
from diagrams.c4 import System, Relationship


def create_diagram(filename, interfaces=None):
	if interfaces is None:
		interfaces = {}
	existing_elements = {}

	graph_attr = {
		"fontsize": "45",
		"bgcolor": "transparent"
	}

	with Diagram(filename=filename, show=False, graph_attr=graph_attr):
		for i in interfaces:
			source_name = str(i.source)
			destination_name = str(i.destination)

			if source_name not in existing_elements:
				origin = System(name=source_name, description=str(i.source.description), external=i.source.is_external)
				existing_elements[source_name] = origin
			else:
				origin = existing_elements[source_name]

			if destination_name not in existing_elements:
				destination = System(name=destination_name, description=str(i.destination.description),
									 external=i.destination.is_external)
				existing_elements[destination_name] = destination
			else:
				destination = existing_elements[destination_name]

			origin >> Relationship(i.description) >> destination


if __name__ == "__main__":
	filename = NamedTemporaryFile(dir="./").name

	create_diagram(filename)
	with open(filename + ".png", "rb") as f:
		diagram_data = f.read()
