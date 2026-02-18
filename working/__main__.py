
import xml.etree.ElementTree as ET

from . import make_rule, addDscale, addCscale, addCFscale



if __name__ == "__main__":

    filename = "newtest.svg"

    doc, rl = make_rule(xvalue = 2, right = True)

    # Add a dscale
    doc = addDscale(doc, rl)

    # Add a cscale
    doc = addCscale(doc, rl)

    # Add a cfscale
    doc = addCFscale(doc, rl)

    tree = ET.ElementTree(doc)
    tree.write(filename, xml_declaration=True)

    print(f'{filename} created')
