import xml.etree.ElementTree as ET

import math

from dataclasses import dataclass

from .dscale import addDscale

from .cscale import addCscale

from .cfscale import addCFscale


@dataclass
class Rule:
    "Defines a rule dimensions"

    scalewidth:int = 900
    topruleheight:int = 120
    midruleheight:int = 200
    btmruleheight:int = 120

    leftmargin:int = 50
    rightmargin:int = 50

    mainmove:float = 0.0
    slidermove:float = 0.0

    def set_movement(self, xvalue, right):

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


    @property
    def imagewidth(self):
        return self.mainmove + self.slidermove + self.leftmargin + self.scalewidth + self.rightmargin

    @property
    def rulewidth(self):
        return self.leftmargin + self.scalewidth + self.rightmargin

    @property
    def imageheight(self):
        return self.topruleheight + self.midruleheight + self.btmruleheight



def make_rule(xvalue = 1, right = True):
    """"xvalue is the x value to set the rule at
        right is True if setting the slider position to the right, in which the 1 goes above the x value 
              or False if slider goes to the left, in which the 10 goes above the x value"""

    if xvalue<1 or xvalue>10:
        raise ValueError("Invalid x value, must be between 1 and 10")

    rl = Rule()
    rl.set_movement(xvalue, right)
    width = rl.rulewidth

    # Start the document
    doc = ET.Element('svg', width=str(rl.imagewidth), height=str(rl.imageheight), version='1.1', xmlns='http://www.w3.org/2000/svg')
    textstyle = ET.SubElement(doc, 'style')
    textstyle.text = """text {
      font-family: Arial, Helvetica, sans-serif;
      font-weight: Thin;
      }
"""
    # top rule

    ### rectangle of background colour
    ET.SubElement(doc, 'rect', {"width":str(width), "height":str(rl.topruleheight), "x":str(rl.mainmove),"y":"0", "fill":"#f9fc69"})

    # bottom line
    ET.SubElement(doc, 'line', {"x1":str(rl.mainmove), "y1":str(rl.topruleheight), "x2":str(rl.mainmove+width), "y2":str(rl.topruleheight), "style":"stroke:black;stroke-width:1"})


    # slider

    ### rectangle of background colour
    ET.SubElement(doc, 'rect', {"width":str(width), "height":str(rl.midruleheight), "x":str(rl.slidermove),"y":str(rl.topruleheight), "fill":"#f9fc69"})

    # top line
    ET.SubElement(doc, 'line', {"x1":str(rl.slidermove), "y1":str(rl.topruleheight), "x2":str(rl.slidermove+width), "y2":str(rl.topruleheight), "style":"stroke:black;stroke-width:1"})

    # bottom line
    ET.SubElement(doc, 'line', {"x1":str(rl.slidermove), "y1":str(rl.topruleheight+rl.midruleheight), "x2":str(rl.slidermove+width), "y2":str(rl.topruleheight+rl.midruleheight), "style":"stroke:black;stroke-width:1"})


    # bottom rule

    heightofy = rl.topruleheight + rl.midruleheight

    ### rectangle of background colour
    ET.SubElement(doc, 'rect', {"width":str(width), "height":str(rl.btmruleheight), "x":str(rl.mainmove),"y":str(heightofy), "fill":"#f9fc69"})

    # top line
    ET.SubElement(doc, 'line', {"x1":str(rl.mainmove), "y1":str(heightofy), "x2":str(rl.mainmove+width), "y2":str(heightofy), "style":"stroke:black;stroke-width:1"})


    return doc, rl









