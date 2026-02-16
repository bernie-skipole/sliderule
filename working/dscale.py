import xml.etree.ElementTree as ET

import math




class Dscale:

    "This is on the bottom rule"

    def __init__(self, rl):

        self.rl = rl
        self.height = rl.topruleheight + rl.midruleheight # y value of top of rule

        self.rightmove = rl.mainmove


    def _vertical(self, length, xpos, col="black"):
        return {"x1":str(xpos), "y1":str(self.height), "x2":str(xpos), "y2":str(self.height+length), "style":f"stroke:{col};stroke-width:1"}


    def render(self, doc) -> ET.Element:

        # D mark
        Dmark = ET.SubElement(doc, 'text', {"x":str(self.rightmove + 8), "y":str(self.height+40),"fill":"black", "font-size":"24"})
        Dmark.text = "D"

        # Pi mark
        xpos = round(self.rightmove + self.rl.leftmargin + self.rl.scalewidth*math.log10(math.pi))
        Pimark = ET.SubElement(doc, 'text', {"x":str(xpos-4), "y":str(self.height+55),"fill":"black", "font-size":"16"})
        Pimark.text = "\u03C0"
        ET.SubElement(doc, 'line', self._vertical(40, xpos))

        for r in range(0, 90000+1):
            # r is 0 to 90000   - this is along rule length
            # x is 1 to 10 inclusive
            x = 1 + r/10000
            xpos = round(self.rightmove + self.rl.leftmargin + self.rl.scalewidth*math.log10(x))
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


def addDscale(doc, rl):
    d = Dscale(rl)
    doc = d.render(doc)
    return doc
    

