
import xml.etree.ElementTree as ET

from . import make_rule

from . import addDscale


if __name__ == "__main__":

    filename = "newtest.svg"

    doc, rl = make_rule(xvalue = 2, right = True)

    # Add a dscale
    doc = addDscale(doc, rl)

    tree = ET.ElementTree(doc)
    tree.write(filename, xml_declaration=True)

    print(f'{filename} created')
