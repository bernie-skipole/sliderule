import xml.etree.ElementTree as ET

import math



from .dscale import addDscale

from .cscale import addCscale

from .cfscale import addCFscale

from .dfscale import addDFscale

from .ll3scale import addLL3scale



class Rule:
    "Defines a rule dimensions"


    def __init__(self, xvalue:float = 1.0, right:bool = True, hairline:float=0.0,
                       topruleheight:int = 120,
                       midruleheight:int = 200,
                       btmruleheight:int = 120):
        """"xvalue is the x value on the C scale to set the rule at
            right is True if setting the slider position to the right, in which the 1 goes above the x value 
                  or False if slider goes to the left, in which the 10 goes above the x value
            hairline is zero if it is not to be shown, or a number between 1.0 and 10.0 in which case
            the hairline cursor will be shown over that number on the C scale  """

        self.topruleheight = topruleheight
        self.midruleheight = midruleheight
        self.btmruleheight = btmruleheight

        self.scalewidth = 900
        self.leftmargin = 50
        self.rightmargin = 50

        self.mainmove = 0.0
        self.slidermove = 0.0

        if xvalue<1 or xvalue>10:
            raise ValueError("Invalid x value, must be between 1 and 10")


        if xvalue == 1:
            move = 0
        else:
            move = self.scalewidth*math.log10(10.0/xvalue)   # This is the movement of a rule

        if right:
            self.mainmove = 0.0
            if xvalue == 1:
                self.slidermove = 0.0
            else:
                self.slidermove = self.scalewidth*math.log10(xvalue)   # This is the movement of a rule
        else:
            self.slidermove = 0
            if xvalue == 1:
                self.mainmove = 0.0
            else:
                self.mainmove = self.scalewidth*math.log10(10.0/xvalue)   # This is the movement of a rule

        if hairline:
            if hairline<1 or hairline>10:
                raise ValueError("Invalid hairline value, should be either zero or a number between 1 and 10")
            self.hairline = hairline
        else:
            self.hairline = 0.0

        width = self.rulewidth

        # Start the document
        self._doc = ET.Element('svg', width=str(self.imagewidth), height=str(self.imageheight), version='1.1', xmlns='http://www.w3.org/2000/svg')
        textstyle = ET.SubElement(self._doc, 'style')
        textstyle.text = """text {
          font-family: Arial, Helvetica, sans-serif;
          font-weight: Thin;
          }
    """
        # top rule

        if topruleheight:
            ### rectangle of background colour
            ET.SubElement(self._doc, 'rect', {"width":str(width), "height":str(self.topruleheight), "x":str(self.mainmove),"y":"0", "fill":"#f9fc69"})

            # bottom line
            ET.SubElement(self._doc, 'line', {"x1":str(self.mainmove), "y1":str(self.topruleheight), "x2":str(self.mainmove+width), "y2":str(self.topruleheight), "style":"stroke:black;stroke-width:1"})


        # slider

        ### rectangle of background colour
        ET.SubElement(self._doc, 'rect', {"width":str(width), "height":str(self.midruleheight), "x":str(self.slidermove),"y":str(self.topruleheight), "fill":"#f9fc69"})

        # top line
        ET.SubElement(self._doc, 'line', {"x1":str(self.slidermove), "y1":str(self.topruleheight), "x2":str(self.slidermove+width), "y2":str(self.topruleheight), "style":"stroke:black;stroke-width:1"})

        # bottom line
        ET.SubElement(self._doc, 'line', {"x1":str(self.slidermove), "y1":str(self.topruleheight+self.midruleheight), "x2":str(self.slidermove+width), "y2":str(self.topruleheight+self.midruleheight), "style":"stroke:black;stroke-width:1"})


        # bottom rule

        heightofy = self.topruleheight + self.midruleheight

        ### rectangle of background colour
        ET.SubElement(self._doc, 'rect', {"width":str(width), "height":str(self.btmruleheight), "x":str(self.mainmove),"y":str(heightofy), "fill":"#f9fc69"})

        # top line
        ET.SubElement(self._doc, 'line', {"x1":str(self.mainmove), "y1":str(heightofy), "x2":str(self.mainmove+width), "y2":str(heightofy), "style":"stroke:black;stroke-width:1"})


        # hairline
        if hairline:
            xh = self.mainmove
            ET.SubElement(self._doc, 'line', {"x1":str(self.hairlinepos),
                                        "y1":"0",
                                        "x2":str(self.hairlinepos),
                                        "y2":str(self.imageheight),
                                        "style":"stroke:grey;stroke-width:1"})


        return




    @property
    def hairlinepos(self):
        if not self.hairline:
            return self.mainmove
        return self.mainmove + self.leftmargin + self.scalewidth*math.log10(self.hairline)


    @property
    def imagewidth(self):
        return self.mainmove + self.slidermove + self.leftmargin + self.scalewidth + self.rightmargin

    @property
    def rulewidth(self):
        return self.leftmargin + self.scalewidth + self.rightmargin

    @property
    def imageheight(self):
        return self.topruleheight + self.midruleheight + self.btmruleheight

    def write(self, filename):
        tree = ET.ElementTree(self._doc)
        tree.write(filename, xml_declaration=True)

    def addDscale(self):
        self._doc = addDscale(self._doc, self)

    def addCscale(self):
        self._doc = addCscale(self._doc, self)

    def addCFscale(self):
        self._doc = addCFscale(self._doc, self)

    def addDFscale(self):
        self._doc = addDFscale(self._doc, self)

    def addLL3scale(self):
        self._doc = addLL3scale(self._doc, self)













