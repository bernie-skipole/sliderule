import xml.etree.ElementTree as ET

import math

from .dscale import addDscale

from .cscale import addCscale

from .cfscale import addCFscale

from .dfscale import addDFscale

from .ll3scale import addLL3scale

from .ll2scale import addLL2scale



class Rule:
    "Defines a rule dimensions"


    def __init__(self, xvalue:float = 1.0, right:bool = True, hairline:float=0.0):
        """xvalue is where the C scale index is placed over the D value
           right is True if the mid scale is moved to the right
           right is False if the mid scale is moved to the left
           hairline is the D value on which the hairline cursor is placed, or zero if no hairline is used """

        self.topruleheight = 0   # 120
        self.midruleheight = 0   # 200
        self.btmruleheight = 0   # 120

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

        self._doc = ET.Element('svg', width=str(self.imagewidth), height=str(self.imageheight), version='1.1', xmlns='http://www.w3.org/2000/svg')
        textstyle = ET.SubElement(self._doc, 'style')
        textstyle.text = """text {
          font-family: Arial, Helvetica, sans-serif;
          font-weight: Thin;
          }
    """
        # List of scales to add to the image
        self.scales = []


    def _maketoprule(self):
        "top rule"
        if self.topruleheight:
            ### rectangle of background colour
            ET.SubElement(self._doc, 'rect', {"width":str(self.rulewidth), "height":str(self.topruleheight), "x":str(self.mainmove),"y":"0", "fill":"#f9fc69"})

            # bottom line
            ET.SubElement(self._doc, 'line', {"x1":str(self.mainmove), "y1":str(self.topruleheight), "x2":str(self.mainmove+self.rulewidth), "y2":str(self.topruleheight), "style":"stroke:black;stroke-width:1"})


    def _makemidrule(self):
        "midrule - the slider"
        if self.midruleheight:
            ### rectangle of background colour
            ET.SubElement(self._doc, 'rect', {"width":str(self.rulewidth), "height":str(self.midruleheight), "x":str(self.slidermove),"y":str(self.topruleheight), "fill":"#f9fc69"})
            # top line
            ET.SubElement(self._doc, 'line', {"x1":str(self.slidermove), "y1":str(self.topruleheight), "x2":str(self.slidermove+self.rulewidth), "y2":str(self.topruleheight), "style":"stroke:black;stroke-width:1"})
            # bottom line
            ET.SubElement(self._doc, 'line', {"x1":str(self.slidermove), "y1":str(self.topruleheight+self.midruleheight), "x2":str(self.slidermove+self.rulewidth), "y2":str(self.topruleheight+self.midruleheight), "style":"stroke:black;stroke-width:1"})


    def _makebtmrule(self):
        "bottom rule"
        if self.btmruleheight:
            # bottom rule
            heightofy = self.topruleheight + self.midruleheight
            ### rectangle of background colour
            ET.SubElement(self._doc, 'rect', {"width":str(self.rulewidth), "height":str(self.btmruleheight), "x":str(self.mainmove),"y":str(heightofy), "fill":"#f9fc69"})
            # top line
            ET.SubElement(self._doc, 'line', {"x1":str(self.mainmove), "y1":str(heightofy), "x2":str(self.mainmove+self.rulewidth), "y2":str(heightofy), "style":"stroke:black;stroke-width:1"})


    def _makehairline(self):
        "hairline"
        if self.hairline:
            ET.SubElement(self._doc, 'line', {"x1":str(self.hairlinepos),
                                        "y1":"0",
                                        "x2":str(self.hairlinepos),
                                        "y2":str(self.imageheight),
                                        "style":"stroke:grey;stroke-width:1"})

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
        # set height in the image
        self._doc.set("height", str(self.imageheight))
        self._maketoprule()
        self._makemidrule()
        self._makebtmrule()
        self._makehairline()
        idx = len(self._doc)
        # and add the scales
        for index, scale in enumerate(self.scales):
            self._doc.insert(index+idx, scale)
        tree = ET.ElementTree(self._doc)
        tree.write(filename, xml_declaration=True)

    def _createscale(self, fn, ht, btmrule, midrule, toprule):
        if toprule>-1:
            rightmove = self.mainmove
        elif midrule>-1:
            rightmove = self.slidermove
        elif btmrule>-1:
            rightmove = self.mainmove
        element = fn(self, rightmove)
        if toprule==0:
            if ht>self.topruleheight:
                self.topruleheight = ht
        elif toprule>0:
            element.set("transform", f"translate(0 {toprule})")
            if ht+toprule>self.topruleheight:
                self.topruleheight = ht+toprule
        elif midrule>-1:
            element.set("transform", f"translate(0 {self.topruleheight + midrule})")
            if ht+midrule>self.midruleheight:
                self.midruleheight = ht+midrule
        elif btmrule>-1:
            element.set("transform", f"translate(0 {self.topruleheight + self.midruleheight + btmrule})")
            if ht+btmrule>self.btmruleheight:
                self.btmruleheight = ht+btmrule
        self.scales.append(element)


    def addDscale(self, ht, btmrule=-1, midrule=-1, toprule=-1):
        self._createscale(addDscale, ht, btmrule, midrule, toprule)

    def addCscale(self, ht, btmrule=-1, midrule=-1, toprule=-1):
        self._createscale(addCscale, ht, btmrule, midrule, toprule)

    def addCFscale(self, ht, btmrule=-1, midrule=-1, toprule=-1):
        self._createscale(addCFscale, ht, btmrule, midrule, toprule)

    def addDFscale(self, ht, btmrule=-1, midrule=-1, toprule=-1):
        self._createscale(addDFscale, ht, btmrule, midrule, toprule)

    def addLL3scale(self, ht, btmrule=-1, midrule=-1, toprule=-1):
        self._createscale(addLL3scale, ht, btmrule, midrule, toprule)

    def addLL2scale(self, ht, btmrule=-1, midrule=-1, toprule=-1):
        self._createscale(addLL2scale, ht, btmrule, midrule, toprule)














