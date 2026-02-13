import xml.etree.ElementTree as ET

import math


class TopRule:

    def __init__(self, xvalue = 1):

        self.rulewidth = 900   # should always by 900, to map integers to x values
        self.ruleheight = 120
        self.leftmargin = 50
        self.rightmargin = 30
        self.yellowwidth = self.leftmargin + self.rulewidth + self.rightmargin
        self.yellowheight = self.ruleheight

        if xvalue == 1:
            self.rightmove = 0
        else:
            self.rightmove = self.rulewidth*math.log10(xvalue)   # This is the movement of a rule

    def width(self):
        return self.rightmove + self.yellowwidth


    def _vertical(self, length, xpos, col="black"):
        return {"x1":str(xpos), "y1":str(self.ruleheight), "x2":str(xpos), "y2":str(self.ruleheight-length), "style":f"stroke:{col};stroke-width:1"}


    def render(self, doc) -> ET.Element:

        ### rectangle of background colour
        ET.SubElement(doc, 'rect', {"width":str(self.yellowwidth), "height":str(self.yellowheight), "x":str(self.rightmove),"y":"0", "fill":"#f9fc69"})

        # bottom line
        ET.SubElement(doc, 'line', {"x1":str(self.rightmove), "y1":str(self.ruleheight), "x2":str(self.rightmove+self.yellowwidth), "y2":str(self.ruleheight), "style":"stroke:black;stroke-width:1"})

        # C mark
        Cmark = ET.SubElement(doc, 'text', {"x":str(self.rightmove + 8), "y":str(self.ruleheight-30),"fill":"black", "font-size":"24"})
        Cmark.text = "C"

        # Pi mark
        xpos = round(self.rightmove + self.leftmargin + self.rulewidth*math.log10(math.pi))
        Pimark = ET.SubElement(doc, 'text', {"x":str(xpos-4), "y":"75","fill":"black", "font-size":"16"})
        Pimark.text = "\u03C0"
        ET.SubElement(doc, 'line', self._vertical(40, xpos))

        for r in range(0, 90000+1):
            # r is 0 to 90000   - this is along rule length
            # x is 1 to 10 inclusive
            x = 1 + r/10000
            xpos = round(self.rightmove + self.leftmargin + self.rulewidth*math.log10(x))
            length = 0
            textstr = ''
            fontsize = 16
            texty = 40
            if not r:                   # at x == 1, r = 0
                length = 70
                textstr = "1"
                fontsize = 18
            elif r == 90000:            # at x == 10, r= 90000
                length = 70
                textstr = "10"
                fontsize = 18
            elif r % 10000 == 0:         # at x = 2, 3, etc 
                length = 60
                textstr = str(round(x))
                fontsize = 18
                texty = 50
            elif r % 5000 == 0:         # at x = 1.5, 2.5, 3.5, etc 
                length = 50
                textstr = str(x)
                fontsize = 14
                texty = 65
            elif r % 1000 == 0:         # at x = 1.1, 1.2, etc 
                length = 30
                if r < 10000:           # only do text for x<2, r <10000  
                    textstr = str(x)
                    fontsize = 12
                    texty = 85
            elif r < 20000:             # x < 3, r < 20000
                if r % 500 == 0:        # at x =1.05, 1.15, etc
                    length = 20

            if length:
                vline = self._vertical(length, xpos, col="black")
                ET.SubElement(doc, 'line', vline)
            if textstr:
                # textpos = xpos - round(fontsize*len(textstr)/3)
                if len(textstr) == 1:
                    textpos = xpos - 4    #  textpos This is in pixels
                else:
                    textpos = xpos - 6    # three characters, such as 1.5
                tel = ET.SubElement(doc, 'text', {"x":str(textpos), "y":str(texty),"fill":"black", "font-size":str(fontsize)})
                tel.text = textstr

        return doc



class BottomRule:

    def __init__(self, xvalue = 1):

        self.rulewidth = 900   # should always by 900, to map integers to x values
        self.ruleheight = 120
        self.height = 120      # this is the y value from the top, equal to the height of the top rule
                               # self.ruleheight could have been used for this, since both rulers are the same,
                               # but keeping it separate may allow future scales to be added
        self.leftmargin = 50
        self.rightmargin = 30
        self.yellowwidth = self.leftmargin + self.rulewidth + self.rightmargin
        self.yellowheight = self.ruleheight

        if xvalue == 1:
            self.rightmove = 0
        else:
            self.rightmove = self.rulewidth*math.log10(10.0/xvalue)   # This is the movement of a rule

    def width(self):
        return self.rightmove + self.yellowwidth

    def _vertical(self, length, xpos, col="black"):
        return {"x1":str(xpos), "y1":str(self.height), "x2":str(xpos), "y2":str(self.height+length), "style":f"stroke:{col};stroke-width:1"}


    def render(self, doc) -> ET.Element:

        ### rectangle of background colour
        ET.SubElement(doc, 'rect', {"width":str(self.yellowwidth), "height":str(self.yellowheight), "x":str(self.rightmove),"y":str(self.height), "fill":"#f9fc69"})

        # top line
        ET.SubElement(doc, 'line', {"x1":str(self.rightmove), "y1":str(self.height), "x2":str(self.rightmove+self.yellowwidth), "y2":str(self.height), "style":"stroke:black;stroke-width:1"})

        # D mark
        Dmark = ET.SubElement(doc, 'text', {"x":str(self.rightmove + 8), "y":str(self.height+40),"fill":"black", "font-size":"24"})
        Dmark.text = "D"

        # Pi mark
        xpos = round(self.rightmove + self.leftmargin + self.rulewidth*math.log10(math.pi))
        Pimark = ET.SubElement(doc, 'text', {"x":str(xpos-4), "y":str(self.height+55),"fill":"black", "font-size":"16"})
        Pimark.text = "\u03C0"
        ET.SubElement(doc, 'line', self._vertical(40, xpos))

        for r in range(0, 90000+1):
            # r is 0 to 90000   - this is along rule length
            # x is 1 to 10 inclusive
            x = 1 + r/10000
            xpos = round(self.rightmove + self.leftmargin + self.rulewidth*math.log10(x))
            length = 0
            textstr = ''
            fontsize = 16
            texty = self.height+95 
            if not r:                   # at x == 1, r = 0
                length = 70
                textstr = "1"
                fontsize = 18
            elif r == 90000:            # at x == 10, r= 90000
                length = 70
                textstr = "10"
                fontsize = 18
            elif r % 10000 == 0:         # at x = 2, 3, etc 
                length = 60
                textstr = str(round(x))
                fontsize = 18
                texty = self.height+80
            elif r % 5000 == 0:         # at x = 1.5, 2.5, 3.5, etc 
                length = 50
                textstr = str(x)
                fontsize = 14
                texty = self.height+65
            elif r % 1000 == 0:         # at x = 1.1, 1.2, etc 
                length = 30
                if r < 10000:           # only do text for x<2, r <10000  
                    textstr = str(x)
                    fontsize = 12
                    texty = self.height+40
            elif r < 20000:             # x < 3, r < 20000
                if r % 500 == 0:        # at x =1.05, 1.15, etc
                    length = 20

            if length:
                vline = self._vertical(length, xpos, col="black")
                ET.SubElement(doc, 'line', vline)
            if textstr:
                # textpos = xpos - round(fontsize*len(textstr)/3)
                if len(textstr) == 1:
                    textpos = xpos - 4    #  textpos This is in pixels
                else:
                    textpos = xpos - 6    # three characters, such as 1.5
                tel = ET.SubElement(doc, 'text', {"x":str(textpos), "y":str(texty),"fill":"black", "font-size":str(fontsize)})
                tel.text = textstr

        return doc


def multiply(filename, xvalue = 1, right=True):
    """filename is the name of the SVG file to be created
       xvalue is the x value to set the rule at
       right is True if setting the top rule position to the right, in which the 1 goes above the x value 
             or False if the top rule to the left, in which the 10 goes above the x value"""

    if xvalue<1 or xvalue>10:
        print("Invalid x value, must be between 1 and 10")
        return

    if xvalue == 1:
        tr = TopRule()
        br = BottomRule()
    elif right:
        tr = TopRule(xvalue)
        br = BottomRule()
    else:
        tr = TopRule()
        br = BottomRule(xvalue)

    width = max(tr.width(), br.width())

    height = tr.yellowheight + br.yellowheight

    # Start the document
    doc = ET.Element('svg', width=str(width), height=str(height), version='1.1', xmlns='http://www.w3.org/2000/svg')
    textstyle = ET.SubElement(doc, 'style')
    textstyle.text = """text {
      font-family: Arial, Helvetica, sans-serif;
      font-weight: Thin;
      }
"""

    doc = tr.render(doc)
    doc = br.render(doc)

    tree = ET.ElementTree(doc)
    tree.write(filename, xml_declaration=True)

    print(f'{filename} created')



