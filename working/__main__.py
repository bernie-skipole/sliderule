
import xml.etree.ElementTree as ET

from . import make_rule, addDscale, addCscale, addCFscale, addDFscale



if __name__ == "__main__":

    filename = "withhairline.svg"

    doc, rl = make_rule(xvalue = 8, right = False, hairline=6)

    # Add a dscale
    doc = addDscale(doc, rl)

    # Add a cscale
    doc = addCscale(doc, rl)

    # Add a cfscale
    doc = addCFscale(doc, rl)

    # Add a dfscale
    doc = addDFscale(doc, rl)

    tree = ET.ElementTree(doc)
    tree.write(filename, xml_declaration=True)

    print(f'{filename} created')
